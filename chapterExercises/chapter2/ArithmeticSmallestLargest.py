numberOne = int(input("Enter first number: "))
numberTwo = int(input("Enter second number: "))
numberThree = int(input("Enter third number: "))

sum = numberOne + numberTwo + numberThree
average =float (numberOne + numberTwo + numberThree / 3)
product = numberOne * numberTwo * numberThree

print("The sum is: " , sum)
print("The average is: " , average)
print ("The product is: " , product)

if numberOne > numberTwo and numberOne > numberThree:
	print("The largest value is: " , numberOne)
if numberTwo > numberOne and numberTwo > numberThree:
	print("The largest value is: " , numberTwo)
if numberThree > numberOne and numberThree > numberTwo:
	print("The largest value is: " , numberThree)

if numberOne < numberTwo and numberOne < numberTwo:
	print("The largest value is: " , numberOne)
if numberTwo < numberOne and numberTwo < numberThree:
	print("The largest value is: " , numberTwo)
if numberThree < numberOne and numberThree < numberTwo:
	print("The largest value is: " , numberThree)





