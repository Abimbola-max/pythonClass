firstLargest = 0
secondLargest = 0

for number in range(1, 11):
	number = int(input("Enter number: "))
	if number > firstLargest:
		firstLargest = number
		
	elif firstLargest > secondLargest:
	 	secondLargest = number 

print('The first largest number is ', firstLargest)
print('The second largest number is ', secondLargest)