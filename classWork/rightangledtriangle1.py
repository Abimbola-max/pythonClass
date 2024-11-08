number = int(input('Enter a number: '))

for count in range (1, number + 1):
	for counter in range(1, count + 1):
		print("*", end=" ")
	print()