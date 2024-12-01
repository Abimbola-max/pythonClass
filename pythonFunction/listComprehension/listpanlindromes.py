def is_palindrome(words:list):
	return[item == item[::-1] for item in words]

