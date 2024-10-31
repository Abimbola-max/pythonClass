import random

randomNumber = random.randint(1, 50)

print('Guess a number between 1 and 50')

guess = 0

while guess != randomNumber:
    
    guess = int(input('Enter your guess: '))

    if (guess > randomNumber):
        print('Too high, try again.')

    elif (guess < randomNumber):
        print('Too low, try again.')

    else:
        print('Correct! The number was: ', randomNumber)
