import random

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
	

