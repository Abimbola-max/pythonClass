number = 7

for counter in range(1, number + 1):
        print(" " * (number - counter), " ")
    
	for count in range(counter, 0, -1):
        	print(count, " ")
    
	for count in range(2, counter + 1):
        	print(count, " ")
    
	print()  

for counter in range(number - 1, 0, -1):
        print(" " * (number - counter), " ")
    
	for count in range(counter, 0, -1):
        	print(count, " ")
    
	for count in range(2, counter + 1):
        	print(count, " ")
    
	print() 