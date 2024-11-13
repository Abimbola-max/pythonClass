answer = int(input("Choose a week:\n1. Week 1\n2. Week 2\n3. Week 3\n>>>"))

match (answer):
	case 1: 
		answer2 =int(input("Choose 1: \n1. Day\n2. Day\n3. Day\n>>>"))
		
		match (answer2):
			case 1: 
				print("Day 2")
				
			case 2:
				print("Day 4")

			case 3:
				print("Day 6")

			case _:
				print("Enter valid input")

				
	case 2: 
		answer3 =int(input("Choose 1: \n1. Day\n2. Day\n3. Day\n>>>"))
		
		match (answer3):
			case 1: 
				print("Day 2")
				
			case 2: 
				print("Day 4")
				
			case 3: 
				print("Day 6")
	
			case _:
				print("Enter valid input")

				
	case 3:
		answer4 = int(input("Choose 1: \n1. Day\n2. Day\n3. Day\n>>>"))
	
		match (answer4):
			case 1: 
				print("Day 2")
				
			case 2: 
				print("Day 4")
				
			case 3: 
				print("Day 6")

			case _:
				print("Enter valid input")

	case _:
		print("Enter valid input")



