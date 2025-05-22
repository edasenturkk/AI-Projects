# Function to response chatbot
def cbresponse(userinput):
    
    userinput = userinput.lower()
    
    # Define rules 
    if "hello" in userinput or "hi" in userinput:
        return "Hello! How can I help you. you can ask anything for me if I know I can answers all questions."
    elif "how are you" in userinput:
        return "You know I am robot I can't feel but thanks for question:) What about you?"
    elif "i am good" in userinput:
        return "Perfect :)"    
    elif "what is the weather" in userinput:
        return "The weather is cold because we are in winter and probably in two days snow will come."
    elif "your name" in userinput:
        return "I'm ChatBot and you can ask anything for me."
    elif "time" in userinput:
        from datetime import datetime
        return "Now the time is " + datetime.now().strftime('%H:%M:%S')
    elif "date" in userinput:
        from datetime import datetime
        return "Now the date is " + datetime.now().strftime('%Y-%m-%d')
    elif "what is function?" in userinput:
        return "A function in programming is a block of code that performs a specific task. It takes input (called parameters or arguments), processes that input, and then returns an output (if needed). Functions allow for code reusability, organization, and modularity."
    elif "bye" in userinput or "goodbye" in userinput:
        return "Goodbye! Have a nice day."
    else:
        return "I'm sorry, I don't understand that. Can you please repeat again?"

while True:
    
    userinput = input("Me: ")
    
    # Chatbot response
    chatresponse = cbresponse(userinput)
    print("Chatbot: " + chatresponse)  #only string works
    
    # EXIT
    if "bye" in userinput.lower() or "goodbye" in userinput.lower():
        break

