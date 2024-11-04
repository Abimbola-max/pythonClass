
response = int(input("Enter any number for you to input the gallon used OR Enter the miles driven OR -1 to quit\n"))
sum = 0
avearge = 0

while (response != -1):
	GALLON_USED = float(input("Enter the gallon used: "))
	MILES_DRIVEN = float(input("Enter the miles driven: "))

	MILES_GALLON = MILES_DRIVEN / GALLON_USED
	print(MILES_GALLON)

	sum += MILES_DRIVEN

	OVERALL_AVEARAGE_MILES_GALLON = sum / MILES_GALLON 
	
	

		
	