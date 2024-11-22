def get_vowels(letters):

	vowel_counter = 0

	for counter in letters:
		if counter == "a" or counter == "e" or counter == "i" or counter == "o" or counter == "u":
			vowel_counter += 1

	return vowel_counter