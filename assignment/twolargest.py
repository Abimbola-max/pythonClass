	
largest = 0
secondLargest = 0

for count in range(1,11):
	number = int(input("Enter number: "))

	if (number > largest):
		secondLargest = largest
		largest = number

	elif (number > secondLargest):
		secondLargest = number
		
print("The largest number is: " , largest)
print("The second largest number is: " , secondLargest)