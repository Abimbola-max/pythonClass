def get_numbers(numbers):
	
	even_counter = 0
	odd_counter = 0
	
	for count in numbers:
		if count % 2 != 0:
			odd_counter += 1
			
		else:
			even_counter += 1
	return[odd_counter,even_counter]		

	
numbers = [1,2,3,6,8,10,1]
print(get_numbers(numbers))

def get_numb(numbers):
	numbers = [1,2,3,6,8,10,1]

	return len([x for x in numbers if x % 2 != 0]) 
print(get_numb(numbers))