number = int(input("Enter number of lines: "))

for count in range(2, number + 1):
	for numb in range(2, count + 1):
		print(" ")
		for count in range(number, numb + 1):
			print(numb)


for counter in range (1, number + 1):
	for number in range(1, counter + 1):
		print(number, end=" ")
	print()
		