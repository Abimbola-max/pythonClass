def get_subtractNumbers(number_one, number_two):

	if (number_one > number_two):
		answer = number_one - number_two
	else:
		answer = number_two - number_one
		
	return answer

number_one = 33
number_two = 77

print(get_subtractNumbers(number_one, number_two))
