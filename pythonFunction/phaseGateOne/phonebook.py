def get_contact():
	
	name = input("Enter the name of the person's contact you want to save: ")

	phone_number = int(input("Enter the phone number you want to save: "))

	return {'name': name, 'phone number': phone_number}

def get_options():
	
	options = int(input("1. Add contact\n2. Remove contact\n3. Find contact by phone number\n4. Find contact by first name\n5. Find contact by last name\n6. Edit contact\n>>>>"))

	contacts = []

	

	match(options):
	
		case 1: 
			
		
		case 2:
			if savingContacts == 2:
				contacts.remove(get_contact())
			print("You have successfully removed", name)

		case 3:
			print(find contacts phone number)

		case 4: 
			print(find contact by first nam 	
		case 5:
			find contact by last name
		case _:
	
get_options()

def add_contacts:
	savingContacts = get_contact()
	contacts.append(savingContacts)
	print("You have successfully added", savingContacts['name'])

def remove				
	
			













































































