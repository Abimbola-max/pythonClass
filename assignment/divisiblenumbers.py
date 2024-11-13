number = int(input("Enter number: "))
count = 1

for count in range(1, number, 1):
	count += 1
if (count % 7 == 0 and count % 13 == 0):
	print("There is a number is divisible by " + "7 " + "and " + "13")
else:
	print("This number is not number divisible by " + "7 " + "and " + "13")
	