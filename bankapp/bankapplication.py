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
                exit_app()
            case _:
                raise InputMisMatchException("Invalid Input")

    except InputMisMatchException:
        print("Invalid input. Please enter a number between 1 and 9.")
        main_menu()

def create_account():
    try:
        first_name = input("Please enter your firstname: ")
        last_name = input("Please enter your lastname: ")
        password = input("Please enter password: ")
        account = bank.create_account(first_name, last_name, password)
        print("\n")
        print("*****Account Registered Successfully*****\n")
        print(f"Hello {first_name} {last_name} your account number is {account.account_number}")
    except NullPointerException:
        print("Fields cannot be empty")
    finally:
        main_menu()

def deposit():
    try:
        account_number = int(input("Please enter your account number: "))
        account = bank.find_account(account_number)
        if account is None:
            raise AccountNotFoundException("Account not found")

        amount = int(input("Please enter your amount: "))
        print(account)
        bank.deposit(account_number, amount)
        print("*****Account Deposited Successfully*****")
    except InvalidAmountException as e:
        print(e)
    except AccountNotFoundException as e:
        print(e)
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
    finally:
        main_menu()


def withdraw():
    print("WITHDRAW MONEY")
    amount = int(input("Enter Amount you'd like to withdraw: "))
    account_number = int(input("Enter your account number: "))
    password = input("Enter password: ")

    try:
        bank.withdraw(amount, account_number, password)
        print(f"*****{amount} withdrawn Successfully!*****")
    except InsufficientFundException as e:
        print(e)
    except InvalidPasswordException as e:
        print(e)
    except ValueError:
        print("Enter valid input ")
    except AccountNotFoundException as e:
        print(e)
    finally:
        print("\n")
        main_menu()


def transfer():
    sender = int(input("Enter Account number of the sender: "))
    receiver = int(input("Enter Account number of receiver: "))
    amount = int(input("Enter amount to transfer: "))
    password = input("Enter your password: ")

    try:
        bank.transfer(sender, receiver, amount, password)
        print(f"*****{amount} transferred successfully from {sender} to {receiver}*****")
    except InsufficientFundException as e:
        print(e)
    except InvalidPasswordException as e:
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

    try:
        balance = bank.check_balance(account_number, password)
        print(f"Your Account balance is {balance}")
    except InsufficientFundException as e:
        print(e)
    except InvalidPasswordException as e:
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
        account.update_password(old_password, new_password)
    except InsufficientFundException as e:
        print(e)
    finally:
        main_menu()

def buy_airtime():
    try:
        account_number = int(input("Enter Account Number: "))
        account = bank.find_account(account_number)
        phone_number = input("Enter phone number: ")
        password = input("Enter password: ")
        amount = int(input("Enter amount: "))
        airtime_input = input("What Airtime would you like to buy?\n1. GLO\n2. AIRTEL\n3. MTN\n4. 9-MOBILE")
        match airtime_input:
            case "1":
                account.buy_airtime(amount, phone_number, airtime_input, password)
            case "2":
                account.buy_airtime(amount, phone_number, airtime_input, password)
            case "3":
                account.buy_airtime(amount, phone_number, airtime_input, password)
            case "4":
                account.buy_airtime(amount, phone_number, airtime_input, password)
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
        account.delete_account(account_number, password)
        print("\n*****Account Closed Successfully*****")
    except AccountNotFoundException as e:
        print(e)
    finally:
        main_menu()


def exit_app():
    print("Thank you for using Bibi's Bank")
    sys.exit(0)

main_menu()