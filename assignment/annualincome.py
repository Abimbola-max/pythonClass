annualIncome = float(input("Enter annual income: "))

if (annualIncome <= 9875):
	firstTaxRate = float(0.10 * annualIncome)
	print(f"Your tax rate is {firstTaxRate:.2f}")

elif (annualIncome >= 9876 and annualIncome <= 40125): 
	secondTaxRate = float(0.12 * annualIncome)
	print(f"Your tax rate is {secondTaxRate:.2f}")

elif (annualIncome >= 40126  and annualIncome <= 85525):
	thirdTaxRate = float(0.22 * annualIncome)
	print(f"Your tax rate is {thirdTaxRate:.2f}")

else:
	lastTaxRate = float(0.24 * annualIncome)
	print(f"Your tax rate is {lastTaxRate:.2f}")
		


