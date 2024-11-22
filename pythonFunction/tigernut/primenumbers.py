def get_prime_numbers(number):

	prime_counter = 0

	for count in range(2, number):
		if number % count == 0:
			prime_counter += 1

	if prime_counter == 0:
		return True
	else:
		return False