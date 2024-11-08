rate = 7/100
total = 0
years = int(input("Enter the amount of years: "))
principal_amount = float(input("Enter your investment amount: "))




for number in range(1,years + 1):
	
	amount_on_deposit = (principal_amount * (1 + rate)**years) - principal_amount
	total += amount_on_deposit

	print(f"The amount on deposit after {number} year is {total:.2f}")