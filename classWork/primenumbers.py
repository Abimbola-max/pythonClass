def is_prime (number):
	if number < 2:
		return "number must be greater than 1"
	if number == 2:
		return True 
	for value in range(2, number):
		if number % value == 0:
			return False
	return True

number = int(input('Enter a number: '))
print(is_prime(number))