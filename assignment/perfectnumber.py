number = int(input("Enter a number: "))

count = 1
sum = 0

for count in range(1, number, 1): 
	if (number % count == 0):
		sum += count;	
count +=1		
if (sum == count):
	print("It is a perfect number")
else:
	print("It is not a perfect number")
			