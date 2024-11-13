number = int(input("Enter number: "))

for count in range(1, number, 1):
	print()
	for counter in range(1, count + 1, 1):
		print(counter, end=" ")
	
count +=1

for counts in range (1, number, 1):
	print()
	for counters in range (1, counts + 1,  1):
		print(counters +1- counts, end=" ")
