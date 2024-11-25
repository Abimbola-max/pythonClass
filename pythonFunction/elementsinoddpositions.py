def get_odd_positions(numbers: list):

	oddPosition = []

	for count in range(1, len(numbers)):
		if count % 2 != 0:
			oddPosition = numbers[count]

	return oddPosition

numbers = [2, 1, 3, 5, 6, 7, 9]
print(get_odd_positions(numbers))