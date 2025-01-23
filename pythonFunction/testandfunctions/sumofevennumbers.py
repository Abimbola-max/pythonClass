def get_sum_even_numbers(numbers: list):
	
	even_counter = 0

	for count in numbers:
		if count % 2 ==0:
			even_counter += 1

	return even_counter