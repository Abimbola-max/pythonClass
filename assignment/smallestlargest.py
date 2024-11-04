firstLargest = 0
smallest = 0

for number in range(1, 11):
	number = int(input("Enter number: "))
	if number > firstLargest:
		firstLargest = number
		
	elif firstLargest > smallest:
	 	smallest = number 

print('The first largest number is ', firstLargest)
print('The second smallest number is ', smallest)