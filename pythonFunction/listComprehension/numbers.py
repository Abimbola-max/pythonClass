def get_number(number):

	numbers = []

	for i in range(1, number):
		numbers.append(i)

	return numbers

number = 6

def get_cube(numbers):
	return[(i**3) for i in numbers]

print(get_cube(get_number(number)))

