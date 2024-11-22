def get_anagram_of_strings(first_word, second_word):

	for characters in first_word:
		if characters in second_word:
			return True
		else:
			return False

	

	