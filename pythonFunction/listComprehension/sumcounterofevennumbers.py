def get_even_count(numbers):

	total = 0
	for count in numbers:
		if count % 2 == 0:
			total += 1
	return total

numbers = [1,2,3,4,5,6,7,8,10,12]

def get_sum():
	
	return get_even_count([x for x in numbers])

print(get_sum())
