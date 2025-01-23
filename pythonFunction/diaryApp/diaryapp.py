import datetime

diary_entries = {}
locked = False


def welcome():

	print("Welcome To AppByMeDiary\n")
	print("The next page Displays, Shows And Help You With Your Choice ?\n")

def create_diary():


	user_name = input("Enter your username: ")

	password = input("Enter a password: ")

	confirm_password = input("Confirm password: ")

	if (password == confirm_password):
		print("You have successfully created a diary account!")
	else:
		print("Password does not match, Please try again.")

def lock_diary():

	global locked
	if not locked:
		print("Diary is locked.")
		return

	try:

		password_to_lock = input("Enter password to lock diary: ")

		if (password_to_lock == password):
			print("You have successfully locked your diary.")
		else:
			print("Incorrect password.") 

	except ValueError:
		print("Error!!")

def unlock_diary():
	
	try:
		if locked:

			password_to_unlock = input("Enter password to lock diary: ")

			if (password_to_unlock == password):
				locked = False
				print("You have successfully unlocked your diary.")
			else:
				print("Incorrect password.") 
		else:
			print("Diary is already unlocked.")

	except ValueError:
		print("Error!!")

def add_entry():

	if not locked:
		print("Diary is locked, unlock the diary to add entry")
		return

	entry_title = input("Enter a title for your diary: ")
	entry_date = datetime.date.today().strftime("%Y-%m-%d")
	entry_text = input("Enter your secret here, let's start:\n")
	entry_text = diary_entries[(entry_date, entry_title)]
	print("Entry added successfully!")

"""def view_entries():

	
	if not locked:
		print("Diary is locked, unlock the diary to view entry")
		return
	
	if 
"""	


def app_menu():

	welcome()

	choice = 0

	while (choice != 6):

		try:

			choice = int(input("1. Create Diary\n2. Lock Diary\n3. Unlock Diary\n4. Add Entry\n5. View Entry\n6. Exit\n Please select one option >>>>> "))

			print()
        			
			match (choice):
            
				case 1: 
					create_diary()
				case 2: 
					lock_diary()
				case 3: 
					unlock_diary()
				case 4:
					add_entry()
				case 5: 
					view_entry()
				case 6:
                    			print("Exiting the diary...") 
				case _:
                    			print("Invalid choice. Please enter a number between 1 and 4.")

		except ValueError:
			print("Invalid input. Please enter a number")

if __name__ == '__main__':
	app_menu()