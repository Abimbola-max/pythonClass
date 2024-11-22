def get_factorial_of_numbers(numbers):

	factorial = 1

	for count in range(numbers, 0, -1):
		factorial *= count 
	return factorial