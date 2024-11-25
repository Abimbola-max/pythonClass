def get_factorial(number):

	factorial = 1
		
	for count in range(number, 1, -1):
		factorial *= count

	return factorial

number = 6
print(get_factorial(number))