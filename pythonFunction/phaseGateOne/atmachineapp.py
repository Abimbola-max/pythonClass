choice = True

while (choice):	

	print("Welcome to the ATM!")
	print("1. create an Account and generate account number")
	print("2. Deposit")
	print("3. Withdraw")
	print("4. Check Balance")
	print("5. Change Pin")
	print("6. Transfer to another account")
	print("7. Exit")

	option = input("Choose an option: ")



	match (option) :

		case 1:

			name = input("Enter your first name and last name: ")
			pin = int(input("Enter your pin(4-digits): "))

			if pin < 4 or pin > 5: 
				print("Error, input 4 digits pin")
	
			else: 
				print("you have successfully created an account")

		case 2:

			deposit_amount = float(input("Enter the amount of money you want to deposit"))

			if deposit_amount < 1000:
	
				print("Error! how can you come to deposit less than 1000?")
			else: 
				print("You have successfully deposited", deposit_amount, " into your account")


		case 3:

			withdrawal_amount = int(input("Enter the amount of money you want to withdraw?"))

			if withdrawal_amount < deposit_amount:
				print("You have successfully withdrawn", withdrawal_amount, " from your account")

			else: 
				print("Insufficient funds")


		case 4:

			if withdrawal_amount == 0:

				account_balance = deposit_amount
			else:

				account_balance = deposit_amount - withdrawal_amount

		case 5:

			new_pin = int(input("Enter your new pin: "))

			pin = new_pin

		case 6:
			
			account_to_transfer_to = int(input("Enter the account number you want to transfer to: "))


		new balance = 

			


	
	
































	

