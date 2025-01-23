def get_number_occurrence(numbers, searchElement):

	for count in numbers:
		if (searchElement == count):
			return True	
			
	return False

numbers = [1, 3, 5, 6, 9, 4]
searchElement = 10
print(get_number_occurrence(numbers, searchElement))