
response = int(input("Enter any number for you to input the gallon used OR Enter the miles driven OR -1 to quit\n"))
sum = 0
avearge = 0

while (response != -1):
	gallonUsed = float(input("Enter the gallon used: "))
	milesDriven = float(input("Enter the miles driven: "))

	milesGallon = milesDriven / gallonUsed
	print(milesDriven)

	sum += milesDriven

	overallAverage = sum / milesGallon
	
	

		
	