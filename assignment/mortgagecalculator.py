amount = int(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate: "))
duration = int(input("Enter the duration of loan: "))

RATE_PERCENTAGE = (100 * 12)
NUMBER_OF_MONTHS = 12

time_in_months = duration * NUMBER_OF_MONTHS
monthly_rate = rate/RATE_PERCENTAGE
exponential_rate = (1 + monthly_rate) ** time_in_months

monthly_payment = (monthly_rate * amount * exponential_rate)/(exponential_rate - 1)

print(f"The monthly payment is ", round(monthly_payment, 2))