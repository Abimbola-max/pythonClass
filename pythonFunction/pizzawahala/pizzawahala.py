def  welcome_Message():
	return "Welcome to Iya Moses Pizza joint!! The best pizza you would ever get and i can bet that"

print(welcome_Message())
	
def number_Of_Guest():

	try:


		numberOfGuests = int(input("Enter number of birthday guests: "))

		while (numberOfGuests < 1):
			print("You have entered the wrong input. Please enter a number greater than 1 or equals to 1")
			numberOfGuests = int(input("Enter number of birthday guests: "))
		print(numberOfGuests)
		number = numberOfGuests
		return numberOfGuests
	except ValueError:
		print("Please enter an integer")
		number_Of_Guest()
	
	
	

	


numberOfGuests = number_Of_Guest()
print(numberOfGuests)

def type_Of_Pizza():

	typeOfPizza = int(input("What type of pizza do you want?\n1. Sapa size pizza\n2. small money pizza\n3. big boys pizza\n4. odogwu pizza\n Enter a number >>> "))
		

	match (typeOfPizza):
		case 1: 
			firstTotalSlice = 4
			box = 1
			remaining = 0
			price = 2500

			totalPrice = 1

			if (remaining == 0):
				box = numberOfGuests // firstTotalSlice
				remaining = (numberOfGuests % firstTotalSlice)
				totalPrice = box * price
 
			if (remaining != 0):
				box = 1 + (numberOfGuests // firstTotalSlice)
				remaining = numberOfGuests % firstTotalSlice
				totalPrice = box * price


			return f"You have selected the sapa size pizza\nThe number of boxes you will buy is: {box} \nThe remaining of the slices is: {remaining} \nThe total amount you are paying is: NGN{totalPrice}\nThank you so much for your patronage!! xx"



		case 2:
			secondTotalSlice = 6
			secondBox = 1
			secondRemaining = 0
			secondPrice = 2900
			secondTotalPrice = 1

			if (secondRemaining == 0): 
				secondBox = numberOfGuests // secondTotalSlice;
				secondRemaining = (numberOfGuests % secondTotalSlice)
				secondTotalPrice = secondBox * secondPrice

				
 
			if (secondRemaining != 0): 
				secondBox = 1 + (numberOfGuests // secondTotalSlice)
				secondRemaining = numberOfGuests % secondTotalSlice
				secondTotalPrice = secondBox * secondPrice

				

			return f"You have selected the small money pizza\nThe number of boxes you will buy is: {secondBox} \nThe remaining of the slices is: {secondRemaining} \nThe total amount you are paying is: NGN{secondTotalPrice}\nThank you so much for your patronage!! xx" 
				
		case 3:
			thirdTotalSlice = 8
			thirdBox = 1
			thirdRemaining = 0
			thirdPrice = 4000
			thirdTotalPrice = 1

			if (thirdRemaining == 0):
				thirdBox = numberOfGuests // thirdTotalSlice
				thirdRemaining = (numberOfGuests % thirdTotalSlice)
				thirdTotalPrice = thirdBox * thirdPrice

				
			if (thirdRemaining != 0):
				thirdBox = 1 + (numberOfGuests // thirdTotalSlice)
				thirdRemaining = numberOfGuests % thirdTotalSlice
				thirdTotalPrice = thirdBox * thirdPrice

			return f"You have selected the big boys pizza\nThe number of boxes you will buy is: {thirdBox} \nThe remaining of the slices is: {thirdRemaining} \nThe total amount you are paying is: NGN{thirdTotalPrice}\nThank you so much for your patronage!! xx"

		case 4:
			lastTotalSlice = 12
			lastBox = 1
			lastRemaining = 0
			lastPrice = 5200
			lastTotalPrice = 1

			if (lastRemaining == 0):
				lastBox = numberOfGuests // lastTotalSlice
				lastRemaining = (numberOfGuests % lastTotalSlice)
				lastTotalPrice = lastBox * lastPrice

			if (lastRemaining != 0):
				lastBox = 1 + (numberOfGuests // lastTotalSlice);
				lastRemaining = numberOfGuests % lastTotalSlice;
				lastTotalPrice = lastBox * lastPrice;


			return f"You have selected the odogwu pizza\nThe number of boxes you will buy is: {lastBox} \nThe remaining of the slices is: {lastRemaining} \nThe total amount you are paying is: NGN{lastTotalPrice}\nThank you so much for your patronage!! xx"


		case _:
			print("You have entered an invalid input")


print(type_Of_Pizza())