number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number3 = float(input("Enter third number: "))



if number1 < number2 < number3:
	print(number1, number2 , number3)

elif number1 < number3 < number2:
	print(number1, number3 , number2)

elif number2 < number1 < number3:
	print(number2, number1 , number3)

elif number2 < number3 < number1:
	print(number2, number3 , number1)

elif number3 < number1 < number2:
	print(number3, number1 , number2)

else:
	print(number2, number3 , number1)