celsiusTemperature = float(input('Enter temperature in celsius: '))

if (celsiusTemperature <= 10):
	print("cold")
elif (celsiusTemperature >=  10 and celsiusTemperature <= 25):
	print("warm")
else:
	print("hot")
