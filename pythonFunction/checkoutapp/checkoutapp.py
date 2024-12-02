def input_product_details():
    

    product_names = []
    product_prices = []
    product_quantities = []

    add_item = ""
    while add_item.lower() != "no":
        if add_item.lower() != "no":  
            product_name = input("What did the user buy?: ")
            product_price = float(input("How much per unit: "))
            quantity = int(input("How many pieces: "))

            if product_price <= 0 or quantity <= 0:
                print("Invalid price or quantity. Please try again.")
            else:
                product_names.append(product_name)
                product_prices.append(product_price)
                product_quantities.append(quantity)

        add_item = input("Do you wish to add another item? yes or 'no': ")
        
    return product_names, product_prices, product_quantities
print(input_product_details())

def calculate_and_display_totals(product_names, product_prices, product_quantities):
	total = 0
	for index in range(len(product_names)):
		total += product_prices[index] * product_quantities[index]

	customer_name = input("What is your name? ")
	discount = float(input("\nHow much discount will they get?: "))

	discount_amount = total * (discount / 100)
	vat_amount = (total - discount_amount) * 0.075
	total_price = total - discount_amount + vat_amount

	print(f"\nBill for {customer_name}:")
	print(f"Sub Total: ${total:.2f}")
	print(f"Discount: ${discount_amount:.2f}")
	print(f"VAT (7.5%): ${vat_amount:.2f}")  
	print(f"Total Price: ${total_price:.2f}")


print(calculate_and_display_totals())

