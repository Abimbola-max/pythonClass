number = (input('Enter a five-digit number: '))

if number.isdigit() and len(number) == 5:
	print("The individual digits are:")
    
	for digit in number:
        	print(digit)
else:
    	print("The number entered is not a five-digit number.")