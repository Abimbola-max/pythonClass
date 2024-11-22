def get_palindrome(text):
	
	count = 0
	counter = -1

	while count <= len(text)// 2:
		if text[count] != text[counter]:
			return False
		count += 1
		counter -= 1
		return True