
def get_products():
		

	menuAnswer = int(input("Jessica's Menu Functions, Please Press:\n1. View products\n2. Add to cart \n3. Remove from cart\n4. View cart \n5. Remove cart\n6. Exit\nEnter an option: "))

	
	match (menuAnswer):
		case 1: 
			taskAnswer= int(input("Select one to add to your cart:\n1. Laptop $1000\n2. Phone $500\n3. headphones $100"))
	
	return menuAnswer
		case 2:
			add_to_cart();
		

print(get_products())

def add_to_cart():
	
	products = []
	

	





	


	