def get_contact():
	
	name = input("Enter the name of the person's contact you want to save: ")

	phone_number = int(input("Enter the phone number you want to save: "))

	return {'name': name, 'phone number': phone_number}

def get_options():
	
	options = int(input("1. Add contact\n2. Remove contact\n3. Find contact by phone number\n4. Find contact by first name\n5. Find contact by last name\n6. Edit contact\n>>>>"))

	contacts = []
	
	if options == 1:
		print(add_contacts()) 
	elif options == 2:
		print(remove_contact())
	else:
		print("invalid")

	
get_options()

def add_contacts():
	savingContacts = get_contact()
	contacts.append(savingContacts)
	print("You have successfully added", savingContacts['name'])

def remove_contact():
	name_to_remove = input("Enter the name of of the contact to remove: ")				
	
			













































































