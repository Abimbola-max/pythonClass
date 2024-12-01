def sorted_keys(dict_one):
	
	sorted_dict = {}
	sorted_keys = sorted(dict_one.keys())

	for key in sorted_keys:
		sorted_dict[key] = dict_one[key]

	return sorted_dict
	


dict_one = {"name": "bimbola", "size": "size8", "complexion": "chocolate", "favourite person": "femi", "age": "12"}
print(sorted_keys(dict_one))