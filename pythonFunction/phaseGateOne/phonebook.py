def get_contact():
	
	name = input("Enter the name of the person's contact you want to save: ")

	phone_number = int(input("Enter the phone number you want to save: "))

	return {'name': name, 'phone number': phone_number}

get_contact()

def get_options():

	print("1. Add contact")
	print("2. Remove contact")
	print("3. Find contact by phone number")
	print("4. Find contact by first name")
	print("5. Find contact by last name")
	print("6. Edit contact")

	
get_options()

contacts = []

def add_contacts():
	savingContacts = get_contact()
	contacts.append(savingContacts)
	print("You have successfully added", savingContacts['name'])

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

add_contacts()

def find_contact_by_phone():

	phone_no_to_find = input("Enter phone number to find: ")
	for contact in contacts:
		if contacts['phone_number'] == phone_no_to_find:
			print("contact found ooo", contact)
			return
	print("contact with phone number", phone_no_to_find, "not found")



def find_contact_by_first_name():

	first_name_to_find = input("Enter the first name to find: ")

	for first_name in contacts:
		if first_name_to_find in contacts['name']:
			print("contact found ooo", first_name)
			return
	print("contact with first name", first_name_to_find , "not found")




def find_contact_by_last_name():

	last_name_to_find = input("Enter the last name to find: ")

	for last_name in contacts:
		if last_name_to_find in contacts['name']:
			print("contact found ooo", last_name)
			return
	print("contact with last name", last_name_to_find, "not found")


def edit_contact():

	
	name_to_edit = input("Enter the last name to find: ")

	for edit_name in contacts:
		if contacts[edit_name]['name'] == name_to_edit:
			print("Current contact details:", contacts[edit_name])
			new_name = input("Enter the new name (leave blank to keep current name): ")
			new_phone_number = input("Enter the new phone number (leave blank to keep current number): ")
			if new_name:
				contacts[edit_name]['name'] = new_name
			if new_phone_number:
				contacts[edit_name]['phone_number'] = new_phone_number
			print("Contact updated successfully.")
			return
	print("Contact not found.")

program_running = True

while program_running:
				
	options = get_options()

	match(options):
		case 1:
			add_contact()
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