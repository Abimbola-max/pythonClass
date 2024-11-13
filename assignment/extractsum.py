number = int(input("Enter number: "))

total = 0

while (number > 0):
	lastDigit =  number % 10
	total += lastDigit	
	
	number //= 10

number += 1

print("The sum of numbers is ",  total)


     
