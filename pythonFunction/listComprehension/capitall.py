def get_list(words: list):
	
	uppercased_words = []
	
	for word in words:
		uppercased_words.append(word.capitalize())

	return uppercased_words

words = ['red', 'orange', 'yellow', 'green', 'blue']

print(get_list(words))

def capitalize_first_letters(words):

	"""return[word.title() for word in words]"""
	return[word[0].upper() + word[1:] for word in words]

words = ['red', 'orange', 'yellow', 'green', 'blue']
print(capitalize_first_letters(words))






	