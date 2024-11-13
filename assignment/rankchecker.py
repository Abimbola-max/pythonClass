rank = int(input("Enter a rank 1-4: "))

match (rank): 
	case 1:
		print("Gold Medal")

	case 2:
		print("Silver Medal")

	case 3:
		print("Bronze Medal")
		
	case 4:
		print("Participation Ribbon")

	case _:
		print("Not found, input number from 1-4 to see your rank")
