def get_duplicate_numbers(numbers):

	numbers = []

	for count in range(len(numbers)):
		for number in range(count + 1, len(numbers)):
			if numbers[count] == numbers[number]:
				return True  
	return False