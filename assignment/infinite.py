number = int(input("Enter any number of your choice or -1 to stop: "))
largest = number
smallest = number

while (number != -1):

	number = int(input("Enter any number of your choice or -1 to stop: "))
	if (number > largest and number != -1):
	   largest = number

	if (number < smallest and number != -1):
	   smallest = number
								
print("The smallest number is : ", smallest);
							
print("The largest number is : ", largest);