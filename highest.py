
count = 1
largest = 0

while count <= 10:
	score = int(input(f"Enter number: "))

	if score > 0 and score < 100 :
		if largest < score :
			largest = score
		count+= 1

	else:
		print("invalid input")
 	 

print(f"Largest is {largest}")