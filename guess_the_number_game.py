#This is a game that guesses the number chosen by the player

import random
print('Hello, What is your name')     #ask for player name
name = input()                        #collects player name
print('Well, ' + name + ' I am thinking of a number between 1 and 20')
secretNumber = random.randint(1, 20)   #this selects a secret number between 1 and 20

for guessesTaken in range(1, 7):        #this say the number of guesses that can be taken by the player
    print('Take a guess.')
    guess = int(input())                #this collects the guess and converters it to an integer so it can be compared to secretNumber

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break                           #this is the codition for correct guess!

if guess == secretNumber:
    print('Good job ' + name + ' you have guessed my number in ' + str(guessesTaken) + ' guesses!.')
else:
    print('Nope the number i was thinking of was ' + str(secretNumber))
    
    
