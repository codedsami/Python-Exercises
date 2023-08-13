# -*- coding: utf-8 -*-
from random import randint
print('Welcome to Guessing Game Challenge!,\nGuess the number in least number of guesses possible')

number = randint(1, 100)

foundRightAnswer = False
numOfGuess = 0

print('Guess !!!:')
previousGuess = None

    
while not foundRightAnswer:
    guessedNumber = int(input())

    numOfGuess += 1
    
    if guessedNumber == number:
        print(f'Congratulations! You found it in {numOfGuess} guesses.')
        break
 
    if not type(guessedNumber) == int:
        print('invalid input')
        numOfGuess += 1
        print('Cold')
        
    elif previousGuess != None: 
        if abs(guessedNumber - number) < abs(previousGuess - number):
            print("Warmer!")
        else:
            print("Colder!")

    elif 1 > guessedNumber or guessedNumber > 100:
        print('OUT OF BOUNDS')
        print('Cold')

    elif abs(guessedNumber - number) < 10:
        print("Warm")

    elif abs(guessedNumber - number) > 10:
        print("Cold")
    
    previousGuess = guessedNumber

    
    
            

    

    
    
    
        
    
