print("Enter student grades (1 for pass, 2 for fail, -1 to stop)")

passes = 0
failures = 0

result = int(input("Enter result (1=pass, 2=fail): "))

while (result != -1):
	if (result == 1):
		passes += 1

	elif (result ==2):
		failures += 1
	else:
		print("Invalid input. Please enter 1 for pass, 2 for fail, or -1 to stop.")

	result = int(input("Enter result (1=pass, 2=fail): "))

print('passed:' , passes)
print('failed:' , failures)



