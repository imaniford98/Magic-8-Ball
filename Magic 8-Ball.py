# This is where the code is going to be.
import random
import time
pip install customtkinter

responses = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Do not count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."]


def play_game():
    inp = input('What would you like to ask the mighty magic 8 ball? ')
    print("You asked: '" + str(inp) + "'")
    time.sleep(1)
    print("Let me check... ")
    time.sleep(1.25) 
    print("...Still thinking... ")
    time.sleep(2)
    print("...Sorry I don't understand... ")
    time.sleep(1.5)
    print("...Here we go... ")
    time.sleep(2)
    print(responses[random.randint(0, len(responses) - 1)])
    play_again()  

def play_again():
    quest = input("Would you like to ask another question? ")
    if quest == 'yes':
        print('')
        play_game()
    elif quest != 'yes':
        print('')
        time.sleep(1.5)
        print('...Goodbye human ...')
        quit()
    if quest =='no':
        prnt('')
        play_game()
    elif quest !='no':
        print('')
        time.sleep(1)
        print('...Have a good day...')
        quit()
play_game()
