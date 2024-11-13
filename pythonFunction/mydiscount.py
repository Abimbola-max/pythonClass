def my_discount(price, discount):
	
	discountAfterPrice = float(price - ((discount / 100) * price)) 

	if discount >= 100:
		return 0
	else:
		return discountAfterPrice
	