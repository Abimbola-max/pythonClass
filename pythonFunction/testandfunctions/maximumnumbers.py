def get_maximum_numbers(numbers: list):

	largest = numbers

	for count in range(len(numbers)):

		if (numbers[count] > largest):

		if (count > largest):

			largest = numbers

	return largest	


numbers = [120, 5, 54, 67, 87, 100]
print(get_maximum_numbers(numbers))