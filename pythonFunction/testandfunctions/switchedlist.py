def get_switched_list(number_one: list, number_two:int):

	for count in number_one:
		for number_two in number_one:
			number_one.append(number_one)

	return number_one

	