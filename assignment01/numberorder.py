number_one = int(input("Enter first number: "))
number_two = int(input("Enter second number: "))
number_three = int(input("Enter third number: "))

if (number_one < number_two < number_three):
	print("This is in increasing order")
elif (number_one > number_two > number_three):
	print("This is in decreasing order")
else:
	print("Numbers not in order")