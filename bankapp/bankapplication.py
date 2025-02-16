import sys

from bankapp.Exception import InputMisMatchException, NullPointerException, InvalidAmountException, \
    InvalidPasswordException, AccountNotFoundException, InsufficientFundException
from bankapp.bank import Bank

bank = Bank()

def main_menu():
    try:
        print(f"""
                              Welcome To Bibi's Bank!
                              1-> Register Account
                              2-> Deposit
                              3-> Withdraw
                              4-> Transfer
                              5-> Check Balance
                              6-> Update Password
                              7-> Buy Airtime
                              8-> Close Account
                              9-> Number of Registered Accounts
                              9-> Exit App
                              """)

        user_input = int(input("Select an option: "))
        match user_input:
            case 1:
                create_account()
            case 2:
                deposit()
            case 3:
                withdraw()
            case 4:
                transfer()
            case 5:
                check_balance()
            case 6:
                update_password()
            case 7:
                buy_airtime()
            case 8:
                close_account()
            case 9:
                number_of_customers()
            case 10:
                exit_app()
            case _:
                raise InputMisMatchException("Invalid Input")

    except ValueError:
        print("Invalid input. Please enter a number between 1 and 9.")
        main_menu()

def create_account():
    try:
        first_name = input("Please enter your firstname: ")
        last_name = input("Please enter your lastname: ")
        password = input("Please enter password: ")
        if not first_name or not last_name or not password:
            raise NullPointerException("Fields cannot be empty")
        account = bank.create_account(first_name, last_name, password)
        print("\n")
        print("*****Account Registered Successfully*****\n")
        print(f"Hello {first_name} {last_name} your account number is {account.account_number}")
    except NullPointerException as e:
        print("Check inputs, might be empty")
    finally:
        main_menu()

def deposit():
    try:
        account_number = int(input("Please enter your account number: "))
        bank.find_account(account_number)
        amount = int(input("Enter Amount you'd like to deposit: "))
        if not account_number or not amount:
            raise NullPointerException("Fields cannot be empty")
        bank.deposit(amount, account_number)
        print(f"***** {amount}NGN has been Deposited Successfully*****")
    except InvalidAmountException as e:
        print(e)
    except AccountNotFoundException as e:
        print(e)
    except NullPointerException as e:
        print("Check inputs, might be empty")
    finally:
        main_menu()


def withdraw():
    print("WITHDRAW MONEY")
    try:
        amount = int(input("Enter Amount you'd like to withdraw: "))
        account_number = int(input("Enter your account number: "))
        password = input("Enter password: ")
        if not account_number or not amount or not password:
            raise NullPointerException("Fields cannot be empty")

        bank.withdraw(amount, account_number, password)
        print(f"*****{amount}NGN withdrawn Successfully!*****")
    except InsufficientFundException as e:
        print(e)
    except InvalidPasswordException as e:
        print(e)
    except ValueError:
        print("Enter valid input ")
    except AccountNotFoundException as e:
        print(e)
    except NullPointerException as e:
        print(e)
    finally:
        main_menu()



def transfer():
    try:
        sender_account_number = int(input("Enter Account number of the sender: "))
        receiver_account_number = int(input("Enter Account number of receiver: "))
        amount = int(input("Enter amount to transfer: "))
        password = input("Enter your password: ")
        if not sender_account_number or not receiver_account_number or not amount or not password:
            raise NullPointerException("Fields cannot be empty")

        bank.transfer(sender_account_number, amount, receiver_account_number, password)
        print(f"*****{amount}NGN transferred successfully from {sender_account_number} to {receiver_account_number}*****")
    except InsufficientFundException as e:
        print(e)
    except InvalidPasswordException as e:
        print(e)
    except NullPointerException as e:
        print(e)
    except ValueError:
        print("Enter valid input ")
    except AccountNotFoundException as e:
        print(e)
    finally:
        main_menu()



def check_balance():
    print("BALANCE")
    account_number = int(input("Enter Account Number: "))
    password = input("Enter password: ")
    if not account_number or not password:
        raise NullPointerException("Fields cannot be empty")

    try:
        balance = bank.check_balance(account_number, password)
        print(f"Your Account balance is {balance}NGN")
    except InsufficientFundException as e:
        print(e)
    except InvalidPasswordException as e:
        print(e)
    except NullPointerException as e:
        print(e)
    except ValueError:
        print("Enter valid input ")
    except AccountNotFoundException as e:
        print(e)
    finally:
        main_menu()

def update_password():
    try:
        account_number = int(input("Enter Account Number: "))
        account = bank.find_account(account_number)
        old_password = input("Enter old password: ")
        new_password = input("Enter new password: ")
        if not account_number or not account or not old_password or not new_password:
            raise NullPointerException("Fields cannot be empty")
        account.update_password(old_password, new_password)
        print("Your password has been updated successfully")
    except InvalidPasswordException as e:
        print("Passwords don't match")
    except NullPointerException as e:
        print(e)
    finally:
        main_menu()

def buy_airtime():
    try:
        account_number = int(input("Enter Account Number: "))
        account = bank.find_account(account_number)
        if not account:
            raise AccountNotFoundException("Account not found.")

        phone_number = input("Enter phone number: ")
        password = input("Enter password: ")
        amount = int(input("Enter amount: "))

        if amount <= 0:
            raise ValueError("Amount must be positive.")

        airtime_input = input(
            "What Airtime would you like to buy?\n1. GLO\n2. AIRTEL\n3. MTN\n4. 9-MOBILE\nEnter your choice (1-4): ")

        airtime_providers = {
            "1": "GLO",
            "2": "AIRTEL",
            "3": "MTN",
            "4": "9-MOBILE"
        }

        airtime_provider = airtime_providers.get(airtime_input)
        if not airtime_provider:
            raise ValueError("Invalid airtime selection.")

        account.buy_airtime(amount, phone_number, airtime_provider, password)
        print("Airtime purchase successful")

    except InsufficientFundException as e:
        print(e)
    except InvalidPasswordException as e:
        print(e)
    except AccountNotFoundException as e:
        print(e)
    finally:
        main_menu()

def close_account():
    try:
        account_number = int(input("Enter Account Number: "))
        account = bank.find_account(account_number)
        password = input("Enter password: ")
        bank.delete_account(account_number, password)
        print("\n*****Account Closed Successfully*****")
    except AccountNotFoundException as e:
        print(e)
    finally:
        main_menu()

def number_of_customers():
    ADMIN_PIN = 2205
    try:
        pin1 = int(input("Enter PIN: "))
        if ADMIN_PIN != pin1:
            print("Invalid PIN")
            return
        else:
            print("Number of registered customers are:")
            number_of_accounts = bank.get_number_of_accounts()
            print(number_of_accounts)
    except ValueError:
        print("Enter a valid PIN")
    finally:
        main_menu()


def exit_app():
    print("Thank you for using Bibi's Bank")
    sys.exit(0)

main_menu()