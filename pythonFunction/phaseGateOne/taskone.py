import random

def get_answer_after_addition():

	first_number = random.randrange(1, 100)
	second_number = random.randrange(1, 100)

	response = int(input(f"What is {first_number} + {second_number}? "))

	correct_answer = first_number + second_number

    
	if response == correct_answer:
		print(True)  
	else:
		print(False)  

get_answer_after_addition()        
        
	