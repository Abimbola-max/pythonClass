answer = int(input("Choose a dessert:\n1. Ice Cream\n2. Sundae\n3. Shake\n>>>"))
		
match (answer):
	case 1: 
		answer2 = int(input("Select your flavor :\n1. Chocolate\n2. vanila\n3. Strawberry\n>>>"))
				
		match (answer2):
			case 1: 
				print("You have chosen Ice cream with Chocolate flavor!!!")
				
			case 2: 
				print("You have chosen Ice cream with Vanilla flavor!!!")
				
			case 3: 
				print("You have chosen Ice cream with Strawberry flavor!!!")

			case _:
				print("Enter valid input")

		
	case 2: 
		answer3 = int(input("Select your flavor :\n1. Chocolate\n2. vanila\n3. Strawberry\n>>>"))
				
		match (answer3):
			case 1: 
				print("You have chosen Sundae with Chocolate flavor!!!")
				
			case 2:
				print("You have chosen Sundae with Vanilla flavor!!!")
				
			case 3: 
				print("You have chosen Sundae with Strawberry flavor!!!")

			case _:
				print("Enter valid input")
	
		

	case 3: 
		answer4 = int(input("Select your flavor :\n1. Chocolate\n2. vanila\n3. Strawberry\n>>>"))
		match (answer4):
			case 1: 
				print("You have just chosen Shake with Chocolate flavor!")
				
			case 2: 
				print("You have just chosen Shake with Vanilla flavor!")
				
			case 3: 
				print("You have just chosen Shake with Strawberry flavor!")
			
			case _:
				print("Enter valid input")


	case _:
		print("Enter valid input")







