def get_odd_even(numbers: list):
		
	result = []

	for count in numbers:
		if count % 2 == 0:
			result.append(True)
		else:
			result.append(False)
	return result