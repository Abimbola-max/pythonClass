def welcome():

	print("Welcome To AppByMeDiary\n")
	print("The next page Displays, Shows And Help You With Your Choice ?\n")

def create_diary():

	global password

	user_name = input("Enter your username: ")

	password = input("Enter a password: ") 

def lock_diary():


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

		password_to_unlock = input("Enter password to lock diary: ")

		if (password_to_unlock == password):
			print("You have successfully unlocked your diary.")
		else:
			print("Incorrect password.") 

	except ValueError:
		print("Error!!")
		


def app_menu():

	welcome()

	choice = 0

	while (choice != 6):

		try:

			choice = int(input("1. Create Diary\n2. Lock Diary\n3. Unlock Diary\n4. Update Diary\n5. Find Entry\n6. Exit\n Please select one option >>>>> "))

			print()
        			
			match (choice):
            
				case 1: 
					create_diary()
				case 2: 
					lock_diary()
				case 3: 
					unlockDiary();break;
				case 4:
					updateDiary(); break;
				case 5: 
					findEntry(); break;
				case 6:
                    			print("Exiting the diary...") 
				case _:
                    			print("Invalid choice. Please enter a number between 1 and 4.")

		except ValueError:
			print("Invalid input. Please enter a number")

if __name__ == '__main__':
	app_menu()