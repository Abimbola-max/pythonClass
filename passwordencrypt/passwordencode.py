import bcrypt

USER_DETAILS = 'user_details.txt'

def hash_passwrd(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def save_to_file(username, hashed_password):
    with open(USER_DETAILS, 'a') as file:
        file.write(f"{username}: {hashed_password.decode('utf-8')}\n")

def register_user():
    while True:
        username = input('Enter username: ')
        if not username:
            print('Username cannot be blank')
            continue
        break

    while True:
        password = input('Enter password: ')
        if not password:
            print('Password cannot be blank')
            continue
        break

    save_to_file(username, hash_passwrd(password))


def validate_username(username, password):
    with open(USER_DETAILS, 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(':')
            if username == stored_username:
                return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))


def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if validate_username(username, password):
        print('Login successful')
    else:
        print('Invalid credentials')

def main():
    menu = """
     1. to register user
     2. to login user
     3. to exit: 
     """
    choice = input(menu)
    match choice:
        case "1":
            register_user()
        case "2":
            login_user()
        case "3":
            print("Thank you!")

main()