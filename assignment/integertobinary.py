number = int(input("Enter number: "))

binary = ''
while number != 0:
	remainder = number % 2
	number //= 2
	binary = str(remainder) + binary

print("Binary number is:", binary)