def get_sum_of_even_numbers(numbers: list): 

	
	sum = 0	

	for count in numbers:
		if count % 2 == 0:
			sum += count
	return sum 

