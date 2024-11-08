number = int(input('Enter a number: '))

if number // 10000 <= 9 and number // 1000 != 0:

	first_digit = number // 10000
	second_digit = (number // 1000) % 10
	third_digit = (number // 100) % 10
	fourth_digit = (number // 10) % 10
	last_digit = number % 10

	if (first_digit == last_digit and second_digit == fourth_digit):
		print(number, "number is a palindrome")
	else:
		print(number, "number is not a palindrome")
else: 
	print('Not valid, please enter the correct number.')

	
