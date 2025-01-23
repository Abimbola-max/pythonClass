def get_prime_numbers(numbers: list):

	prime_counter = []

	is_prime = True
	
	for count in range(2, numbers):
		if numbers % count == 0:
			is_prime = False
			break
	if is_prime:
		prime_counter.append(numbers)

	return prime_counter 
	

	