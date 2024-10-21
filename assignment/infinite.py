number = int (input('Enter number or -1 to quit: '))

smallest = number
largest = number

while number != -1:
	number = int (input('Enter number or -1 to quit: '))
	if number > largest and number != -1:
		largest = number
	if number < smallest and number != -1:
		smallest = number

print ("The largest number is: ", largest)
print ("The smallest number is: ", smallest)