import math
import time
from player import humanplayer, randomcompplayer, smartcompplayer

class TicTacToe():
    def __init__(self):
        self.wood = self.make_wood()
        self.still_winner = None
    
    @staticmethod
    def make_wood():
        return [' ' for _ in range(9)]
    
    def print_wood(self):
        for row in [self.wood[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_wood_nums():
        number_wood = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_wood:
            print('| ' + ' | '.join(row) + ' |')
    
    def start_move(self, square, letter):
        if self.wood[square] == ' ':
            self.wood[square] = letter
            if self.winner(square, letter):
                self.still_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        
        row_id = math.floor(square / 3)
        row = self.wood[row_id*3:(row_id+1)*3]
        
        if all([k == letter for k in row]):
            return True
        col_id = square % 3
        column = [self.wood[col_id+i*3] for i in range(3)]
        
        if all([k == letter for k in column]):
            return True
        if square % 2 == 0:
            diagonal_1 = [self.wood[i] for i in [0, 4, 8]]
            
            if all([k == letter for k in diagonal_1]):
                return True
            diagonal_2 = [self.wood[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([k == letter for k in diagonal_2]):
                return True
        return False
    
    def empty_sqr(self):
        return ' ' in self.wood
    
    def num_emptysqr(self):
        return self.wood.count(' ')
    
    def availablemoves(self):
        return [i for i, x in enumerate(self.wood) if x == " "]

def play(game, xplayer, oplayer, printgame=True):

    if printgame:
        game.print_wood_nums()

    letter = 'X'
    while game.empty_sqr():
        if letter == 'O':
            square = oplayer.move(game)
        else:
            square = xplayer.move(game)
        if game.start_move(square, letter):

            if printgame:
                print(letter + ' makes a move towards the square {}'.format(square))
                game.print_wood()
                print('')

            if game.still_winner:
                if printgame:
                    print(letter + ' WINNN:)')
                return letter 
            letter = 'O' if letter == 'X' else 'X'  
        time.sleep(.8)

    if printgame:
        print('It ended in a draw (TIE)')

if __name__ == '__main__':
    xplayer = smartcompplayer('X')
    oplayer = humanplayer('O')
    t = TicTacToe()
    play(t, xplayer, oplayer, printgame=True)