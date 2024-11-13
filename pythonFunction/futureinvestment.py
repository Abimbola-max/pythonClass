import math

def get_future_investment(investment_amount, monthly_interest_rate, years):

	number_of_months = years * 12

	future_investment_amount = float(investment_amount *  math.pow((1 + monthly_interest_rate),number_of_months))

	return round(future_investment_amount, 2)

	if years < 0:
		return 0

	else:
		return 1