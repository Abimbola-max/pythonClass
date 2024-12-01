def get_values_keys(first_list, second_list):

	both_list = {}

	for key, value in zip(first_list, second_list):
		both_list[key] = value

	return both_list


def only_value(new_list):
		
	return list(value for value in new_list.values())