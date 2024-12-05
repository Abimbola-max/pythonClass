def get_sum_of_doubled_even_place(card_number):

	sum_even = 0

	for number in range(len(card_number) - 2, -1, -2):
		digit = int(card_number[number])
		doubled_digit = digit * 2
		sum_even += get_digit(doubled_digit)

	return sum_even

def get_sum_of_doubled_odd_place(card_number):

	sum_odd = 0

	for number in range(len(card_number) - 1, -1, -2):
		sum_odd += int(card_number[number])

	return sum_odd

def get_digit(number):

	if number > 9:
		return number - 9
	else:
		return number

def is_valid(card_number):

	if len(card_number) >= 13 and len(card_number) <= 16:
		even_sum = get_sum_of_doubled_even_place(card_number)
		odd_sum = get_sum_of_doubled_odd_place(card_number)
		return (even_sum + odd_sum) % 10 == 0

	else:
		return False

card_number = input("Hello, kindly enter your card details to verify: \n")

def print_out():

	print("**************************************")

	if card_number.startswith("5"):
		print("**Credit Card Type: Mastercard")

	elif card_number.startswith("4"):
		print("**Credit Card Type: Visa card")

	elif card_number.startswith("37"):
		print("**Credit Card Type: American Express cards")

	elif card_number.startswith("6"):
		print("**Credit Card Type: Discover card")

	else:
		print("Invalid details")

	if is_valid(card_number):
		print("**Credit card validity Status: valid")

	else:
		print("**Credit card validity Status: invalid")

	print("**Credit Card Number: " + card_number)
	print("**Credit Card Digit Length: " + str(len(card_number)))
	print("**************************************")

print_out()