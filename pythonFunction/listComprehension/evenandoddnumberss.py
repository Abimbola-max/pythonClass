def get_odd_even(numbers: list):
		
	result = []

	for count in numbers:
		if count % 2 == 0:
			result.append(True)
		else:
			result.append(False)
	return result

numbers = [10, 3,7,1,9,4,2,8,5,6]

def get_even_plus_false():
	return get_odd_even([x for x in numbers])

print(get_even_plus_false())


def get_even_odd(numbers):

	return [True if x % 2 == 0 else False for x in numbers]
	return[x % 2 == 0 for x in numbers]

numbers = [1,2,3,4,5,6,7,8,9,10,11]
 
print(get_even_odd(numbers))





