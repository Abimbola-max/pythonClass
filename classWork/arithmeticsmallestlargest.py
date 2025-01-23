number = 0
sum = 0
average = 0
product = 1
smallest = number
largest = number

for number in range(1,5): 
	number = int(input("Enter number: "))
	sum += number
	average = sum / 4
	product *= number
	if smallest < number and smallest != 0:
		number = smallest
	else: 
		number = largest

print ('The sum is ', sum)
print ('The average is ', average)
print ('The product is ', product)
print ('The smallest is ', smallest)
print ('The largest is ', largest)