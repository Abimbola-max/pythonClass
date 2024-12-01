def get_values_keys(first_list, second_list):

	both_list = {}

	for key, value in zip(first_list, second_list):
		both_list[key] = value

	return both_list