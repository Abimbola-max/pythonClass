def get_numbers_in_one(numbers: list):

	result = []
	divisor = 2
	
	middle_index = len(numbers) // divisor
	result.append(numbers[:middle_index])
	result.append(numbers[middle_index:])


	return result
		

		