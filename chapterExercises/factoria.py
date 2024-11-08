number = int(input("Enter number : "))
factoria = 1
while number > 0:
	factoria *= number 
	number = number - 1 
print("answer is ",factoria," Factoria")