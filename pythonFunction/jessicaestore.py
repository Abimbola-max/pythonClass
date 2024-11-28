total = []
cart = []
product = []
mainuserInput = 0



def add_to_cart():
	product = input("Enter the product name or 6 to exit:")
	if product.lower() == 'laptop':
		cart.append("laptop - $1000")
		total.append(1000)
		print("you Added  Laptop - $1000 to cart")
	elif product.lower() == 'phone' :
		cart.append("phone - $500")
		total.append(500)
		print ("you Added  Phone - $500 to cart")
	elif product.lower() == 'headphones' :
		cart.append("headphones - $100")
		total.append(100)
		print ("you Added  Headphones - $100 to cart")
	elif product == '6' :
		main_menu()
	else :
		print("invalid input product missmatch !!!") 
		add_to_cart()	

def remove_from_cart():
	product = input("Enter the product name or 6 to exit:")
	if product.lower() == 'laptop':
		cart.remove("laptop - $1000")
		total.remove(1000)
		print("you Added  Laptop - $1000 to cart")
	elif product.lower() == 'phone':
		cart.remove("phone - $500")
		total.remove(500)
		print ("you Added  Phone - $500 to cart")
	elif product.lower() == 'headphones' :
		cart.remove("headphones - $100")
		total.remove(100)
		print ("you Added  Headphones - $100 to cart")
	elif product == '6' :
		main_menu()
	else :
		print("invalid input product missmatch !!!") 
		add_to_cart()	



def view_cart():
	return print(cart)
		


def check_out():
	checkout = 0
	for money in total:
		checkout += money
	print(f"checkout page \nYour list of purchase \n{view_cart()} \n total is $-{checkout}")
		

	

def view_product():
	return "1. Laptop - $1000 \n2. Phone - $500 \n3. Headphones - $100"

def main_menu():
	userInput = int(input("Welcome to Jessica's E-Store! \n1. View Products \n2. Add to Cart \n3. Remove from Cart \n4. View Cart \n5. Checkout \n6. Exit\nEnter a enter option :"))
	if userInput == 1:
		print(view_product())
	elif userInput == 2:
		add_to_cart()
	elif userInput == 3:
		remove_from_cart()
	elif userInput == 4:
		view_cart()
	elif userInput == 5:
		check_out()

	elif userInput == 6:
		mainuserInput = 6
		
			
while (mainuserInput != 6):
		view_product()
		main_menu()