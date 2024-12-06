option = True
 
def get_options():

	while(option):
	
		print("1. Add contact")
		print("2. Remove contact")
		print("3. Find contact by phone number")
		print("4. Find contact by first name")
		print("5. Find contact by last name")
		print("6. Edit contact")
		print("7. Exit")
		
		try:
			options = int(input("Enter an option: "))

			if 1 <= options or options <= 7:
				return options

			else:
				print("Invalid option. Please enter a number between 1 and 7.")
		except ValueError:
			print("Invalid input. Please enter a number.")


contacts = []

def add_contacts():

	name = input("Enter the name of the person's contact you want to save: ")

	phone_number = int(input("Enter the phone number you want to save: "))

	email_address = input("Enter email address: ")

	contact = {'name': name, 'phone number': phone_number, 'email address': email_address}

	contacts.append(contact)

	print("You have successfully added", contact['name'])


def remove_contact():

	name_to_remove = input("Enter the name of of the contact to remove: ")
	contact_removed = False

	for contact in len(contacts):
		if contacts[contact]['name'] == name_to_remove:
			del contacts[contact]
			contact_removed = True 
			break
	if contact_removed:
		print("You have successfully removed", name_to_remove)	
	else:
		print("We could not find contact")


def find_contact_by_phone():

	phone_no_to_find = input("Enter phone number to find: ")
	contact_found = False

	for contact in contacts:
		if contact['phone_number'] == phone_no_to_find:
			print("contact found ooo", contact)
			contact_found = True
			break
	print("contact with phone number", phone_no_to_find, "not found")



def find_contact_by_first_name():
	first_name_to_find = input("Enter the first name to find: ")
	contact_found = False

	for contact in contacts:
		if first_name_to_find in contact['name'].split():  
			print("Contact found:", contact)
			contact_found = True
			break

	if not contact_found:
		print("Contact with first name", first_name_to_find, "not found.")

def find_contact_by_last_name():
	last_name_to_find = input("Enter the last name to find: ")
	contact_found = False

	for contact in contacts:
		if last_name_to_find in contact['name'].split()[-1]:  
			print("Contact found:", contact)
			contact_found = True
			break

	if not contact_found:
		print("Contact with last name", last_name_to_find, "not found.")

def edit_contact():
	name_to_edit = input("Enter the name of the contact to edit: ")
	contact_found = False

	for count in range(len(contacts)):
		if contacts[count]['name'] == name_to_edit:
			print("Current contact details:", contacts[count])
			new_name = input("Enter the new name (leave blank to keep current name): ")
			new_phone_number = input("Enter the new phone number (leave blank to keep current number): ")
		if new_name:
			contacts[count]['name'] = new_name
		if new_phone_number:
			contacts[count]['phone_number'] = new_phone_number
			print("Contact updated successfully.")
			contact_found = True
			break

		if not contact_found:
			print("Contact not found.")

program_running = True
while program_running:
	options = get_options()
    
	match(options):
		case 1:
			add_contacts()
		case 2:
			remove_contact()
		case 3:
			find_contact_by_phone()
		case 4:
			find_contact_by_first_name()
		case 5:
			find_contact_by_last_name()
		case 6:
			edit_contact()
		case 7:
			program_running = False
		case _: 
			print("Invalid option.") 

