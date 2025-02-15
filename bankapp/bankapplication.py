from bankapp.Exception import InputMisMatchException, NullPointerException
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

    except InputMisMatchException:
        print("Invalid Input")


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

main_menu()