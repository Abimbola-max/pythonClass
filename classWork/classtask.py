number = int(input('Enter number: '))

for count in range(1, number + 1):
	print()
	for number in range(1, count + 1):
		print(number, end=" ")
for counter in range(number, 1, -1):
	print()
	for count in range(1, counter):
		print(count, end=" ")