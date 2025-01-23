def get_reversed_number(numbers: list):

	reversedNumber = []
	
	for count in range(len(numbers) - 1, -1, -1):
		reversedNumber.append(numbers[count])
	return reversedNumber

			
numbers = [1,2,4,6,5,8,7,9]
print(get_reversed_number(numbers))
