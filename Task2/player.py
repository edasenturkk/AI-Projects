import math
import random

class player():
    def __init__(self,letter):
        self.letter=letter
    
    def move(self,game):
        pass

class humanplayer(player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def move(self,game):
        val_sqr=False
        val=None
        while not val_sqr:
            square = input(self.letter + 'Input move (0-9): ')
            try:
                val = int(square)
                if val not in game.availablemoves():
                    raise ValueError
                val_sqr=True
            except ValueError:
               print('Invalid play square. TRY AGAIN!!!')
        return val

class  randomcompplayer(player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def move(self,game):
        square= random.choice(game.availablemoves())
        return square

class smartcompplayer(player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def move(self,game):
        if len(game.availablemoves()) == 9:
            square = random.choice(game.availablemoves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, durum, player):
        maxplayer = self.letter 
        otherplayer = 'O' if player == 'X' else 'X'

        if durum.still_winner == otherplayer:
            return {'position': None, 'score': 1 * (durum.num_emptysqr() + 1) if otherplayer == maxplayer else -1 * (
                        durum.num_emptysqr() + 1)}
        elif not durum.empty_sqr():
            return {'position': None, 'score': 0}

        if player == maxplayer:
            best = {'position': None, 'score': -math.inf}  
        else:
            best = {'position': None, 'score': math.inf}  
        for possiblemove in durum.availablemoves():
            durum.start_move(possiblemove, player)
            s_score = self.minimax(durum, otherplayer)  

            
            durum.wood[possiblemove] = ' '
            durum.still_winner = None
            s_score['position'] = possiblemove  

            if player == maxplayer:  
                if s_score['score'] > best['score']:
                    best = s_score
            else:
                if s_score['score'] < best['score']:
                    best = s_score
        return best
        