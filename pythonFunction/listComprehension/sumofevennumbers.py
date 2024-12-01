
def get_even_sum(numbers):

	return len([x for x in numbers if x % 2 == 0])
	return sum([1 for x in numbers if x % 2 == 0]) 

numbers = [1,2,3,4,5,6,7,8,9,10,11]
 
print(get_even_sum(numbers))



def get_even_sum(numbers):

	total = 0
	for count in numbers:
		if count % 2 == 0:
			total += count
	return total

numbers = [1,2,3,4,5,6,7,8,10]

def get_sum():
	
	return get_even_sum([x for x in numbers])

print(get_sum())

def get_sum(value):

	total = 0

	for i in value:
		total += 1

	return total

def get_even_sum(value):

	return get_sum([x for x in value if x % 2 == 0])


value = [1,2,3,4,4,5,6,6,7,7,8,10]
print(get_even_sum(value))









	