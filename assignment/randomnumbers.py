import random

<<<<<<< HEAD
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
=======
print('enter of a guess from 0-50')

guess = int(input('Enter a guess: '))

randomNumber = random.randint(1, 50)

while (guess != randomNumber):
 
	if (guess > randomNumber):
		print('Too high, try again', ' here is the guessed number ', randomNumber)

	else:
		print('Too low, try again', ' here is the guessed number ', randomNumber)

guess = (input('Enter another guess: '))
	
       if (guess == randomNumber):
	    print('correct', 'here is the guessed number ', randomNumber)
	

>>>>>>> e09ac4a5048366362d45aea5187f030e1998b4c2
