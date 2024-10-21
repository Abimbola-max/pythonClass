number_one = int (input('Enter number: '))
number_two = int (input('Enter number: '))

product = 1
for _ in range (1, number_two + 1):
	product *= number_one

print (product)
