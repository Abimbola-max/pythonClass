count = 1
while count < 3:
	name = str(input('Enter name: '))

	earnings = int(input('Enter earnings ' + name + ': '))

	if (earnings > 30000):
		low_rate = 0.15 * earnings
		print("Your total tax is ", low_rate)

	else:
		high_rate = 0.20 * earnings
		print("Your total tax is ", high_rate)