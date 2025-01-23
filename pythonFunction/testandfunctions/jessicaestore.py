total = []
cart = {}  # Use a dictionary to store product counts
product = []
mainUserInput = 0

def add_to_cart():
    product = input("Enter the product name or 6 to exit: ")
    if product.casefold() == 'laptop':
        if 'laptop' in cart:
            cart['laptop'] += 1
        else:
            cart['laptop'] = 1
        total.append(1000)
        print("You added Laptop - $1000 to cart")
    elif product.casefold() == 'phone':
        if 'phone' in cart:
            cart['phone'] += 1
        else:
            cart['phone'] = 1
        total.append(500)
        print("You added Phone - $500 to cart")
    elif product.casefold() == 'headphones':
        if 'headphones' in cart:
            cart['headphones'] += 1
        else:
            cart['headphones'] = 1
        total.append(100)
        print("You added Headphones - $100 to cart")
    elif product == '6':
        exit()
    else:
        print("Invalid input product mismatch !!!")
        add_to_cart()

def remove_from_cart():
    product = input("Enter the product name or 6 to exit: ")
    if product.casefold() == 'laptop':
        if 'laptop' in cart and cart['laptop'] > 0:
            cart['laptop'] -= 1
            total.remove(1000)
            print("Laptop has been removed from your cart (Laptop - $1000)")
        else:
            print("Laptop is not in your cart.")
    elif product.casefold() == 'phone':
        if 'phone' in cart and cart['phone'] > 0:
            cart['phone'] -= 1
            total.remove(500)
            print("Phone has been removed from your cart (Phone - $500)")
        else:
            print("Phone is not in your cart.")
    elif product.casefold() == 'headphones':
        if 'headphones' in cart and cart['headphones'] > 0:
            cart['headphones'] -= 1
            total.remove(100)
            print("Headphones have been removed from your cart (Headphones - $100)")
        else:
            print("Headphones are not in your cart.")
    elif product == '6':
        exit()
    else:
        print("Invalid input product mismatch !!!")
        remove_from_cart()

def view_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        for item, count in cart.items():
            print(f"{item}: {count}")

def check_out():
    checkout = 0
    for money in total:
        checkout += money
    print("Checkout page")
    print("Your list of purchases:")
    view_cart()  # Display cart contents
    print(f"\nTotal is $-{checkout}")
    print("Thank you for shopping with us!!!")
    exit()

def main_menu():
    global mainUserInput
    while mainUserInput != 6:
        print("\n **Main Menu**")
        print("1. Add to cart")
        print("2. Remove from cart")
        print("3. View cart")
        print("4. Checkout")
        print("6. Exit")
        
        try:
            mainUserInput = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid Input! Please enter a number.")
            continue

        if mainUserInput == 1:
            add_to_cart()
        elif mainUserInput == 2:
            remove_from_cart()
        elif mainUserInput == 3:
            view_cart()
        elif mainUserInput == 4:
            check_out()
        elif mainUserInput == 6:
            print ("Thank you for shopping with us!!!")
            exit()
        else:
            print("Invalid choice. Please try again.")

# Start the program
main_menu()