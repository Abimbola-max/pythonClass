def get_square_of_even_odd(numbers):

	
	return[(x ** 2) for x in numbers if x % 2 != 0]

numbers = [10,3,7,1,9,4,2,8,5,6]
 
print(get_square_of_even_odd(numbers))
