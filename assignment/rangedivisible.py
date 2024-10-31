starting_point = int(input("Enter starting point of range: "))
end_point = int(input("Enter end point of range: "))
given_value = int(input("Enter given value: "))

count = 0

for numbers in range (starting_point, end_point + 1):
	if numbers % given_value == 0:
		count +=1
print(count)