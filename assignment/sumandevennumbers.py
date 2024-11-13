sum = 0;
		
for count in range(1, 2):
	
	number = int(input("Enter number: "))

	for counter in range (2, number + 1, 1):
		count +=1

		if (count % 2 == 0):
			sum += count;				
count += 1

print("The sum of all even numbers are: ",  sum);

