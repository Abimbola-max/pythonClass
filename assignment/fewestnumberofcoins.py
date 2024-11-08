purchase_price = int(input('Enter purchase price: '))

if purchase_price < 0 or purchase_price > 1:
        print("Error: Purchase price must be between 0 and 1 dollar.")

change = round((1.00 - purchase_price) * 100)  
   
quarters = change 
change %= 25

dimes = change 
change %= 10

nickels = change 
change %= 5

pennies = change

print("Your change is:")
    
if quarters > 0:
        print(f"{quarters} quarter{'s' if quarters > 1 else ''}")
        
if dimes > 0:
        print(f"{dimes} dime{'s' if dimes > 1 else ''}")
        
if nickels > 0:
        print(f"{nickels} nickel{'s' if nickels > 1 else ''}")
        
if pennies > 0:
        print(f"{pennies} penn{'y' if pennies == 1 else 'ies'}")