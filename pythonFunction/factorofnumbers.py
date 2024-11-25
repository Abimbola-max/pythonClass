def get_number_of_factors(number):

	factor_count = 0

	for count in range(1, number + 1):
		if number % count == 0:
			factor_count += 1

	return factor_count

number = 10
print(get_number_of_factors(number))