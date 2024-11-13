answer = int(input("Choose a department:\n1. IT\n2. HR\n3. Finance\n>>>"))

match (answer):
	case 1:
		answer2 = int(input("Select your Role:\n1. Manager\n2. Analyst\n3. Intern\n>>>"))
		
		match (answer2):
			case 1:
				print("You are the Manager in the IT department")

			case 2: 
				print("You are the Analyst in the IT department")
				
			case 3:
				print("You are an Intern in the IT department")

			case _:
				print("Enter valid input")
	
				
	case 2: 
		answer3 = int(input("Select your Role:\n1. Manager\n2. Analyst\n3. Intern\n>>>"))
		
		match (answer3):
			case 1: 
				print("You are the Manager in the HR department")

			case 2: 
				print("You are the Analyst in the HR department")

			case 3:
				print("You are an Intern in the HR department")	

			case _:
				print("Enter valid input")

				
	case 3: 
		answer4 =int(input("Select your Role:\n1. Manager\n2. Analyst\n3. Intern\n>>>"))
				
		match (answer4):
			case 1:
				print("You are the Manager in the Finance department")

			case 2: 
				print("You are the Analyst in the Finance department")

			case 3:
				print("You are an Intern in the Finance department")

			case _:
				print("Enter valid input")


	case _:
		print("Enter valid input")
	
				