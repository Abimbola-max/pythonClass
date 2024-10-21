positive_count = 0
negative_count= 0
zero_count = 0
for count in range(1,6):
	number = int(input("Enter a number: "))


	if number > 0:
		positive_count += 1
	elif number < 0:
		negative_count+= 1
	else:
		zero_count+= 1

print(f"There are {positive_count} positive numbers, There are {negative_count} negative numbers, There are {zero_count} zero numbers")

		
	


