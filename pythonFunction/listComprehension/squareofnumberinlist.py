def get_square_of(number):
	result = []
	for count in range(1, 5):
		result.append(count**2)
	return result



def get_square(number):
	return(get_square_of([i for i in range(1,5)]))

print(get_square(4))
