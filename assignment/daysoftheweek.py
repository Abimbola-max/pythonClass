reply = int(input("Enter a number within 1-7: "))

match (reply) :
	case 1:
		print("Monday")

	case 2:
		print("Tuesday") 

	case 3:
		print("Wednesday")
		
	case 4:
		print("Thursday")

	case 5:
		print("Friday")

	case 6:
		print("Saturday")

	case 7:
		print("Sunday")
	case _:
		print("Not found, input number from 1-7")

