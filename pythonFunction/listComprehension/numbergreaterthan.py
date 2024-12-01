def get_greater_than(numbers:list):

	result = []

	for count in numbers:
		if count > 10:
			result.append(count)
	return result

def get_number_greater(numbers: list):

	return(get_greater_than([i for i in numbers]))

print(get_number_greater([1,5,12,15,8]))