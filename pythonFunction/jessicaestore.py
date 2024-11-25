userInput =int(input('Welcome to Jessicas E-Store! /n1. View Products /n2. Add to Cart /n3. Remove from Cart /n4. View Cart /n5. Checkout /n6. Exit'))
match(userInput):
	case 1 :
		view_product()
	case 2 : 
		add_to_cart()
	case 3 :
	case 4 :
	case 5 :
	case 6 :
	case_ :

def view_product():
	sellectedProduct = int(input(1. Laptop - $1000 /n2. Phone - $500 /n3. Headphones - $100))
	match selectedProduct:
		case 1: add_to_cart([1000],"Laptop - $")
		case 2: add_to_cart(["500"], "Phone - $"])
		case 3: add_to_cart([100],["Headphones - $"])

def add_to_cart(cart:str,products:int):
	prices = []
	product =[]
	prices.append(cart)
	product.append(products)
	return f"{products} has been added to your cart"
def remove_cart():