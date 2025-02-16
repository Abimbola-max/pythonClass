import sys

from bankapp.Exception import NullPointerException
from diaryapplication import diaries, entry, diary
from diaryapplication.diaries import Diaries
from diaryapplication.diary import Diary
from diaryapplication.exception import LockedStateException, NotFoundException


class DiaryApp:

    def __init__(self):
        self.my_diary = Diary('username', 'password')
        self.my_diaries = Diaries()

    def main_menu(self):
        self.welcome()
        print("""
            1 --> Create Diary
            2 --> Create Entry
            3 --> Find Entry By Id
            4 --> Update Entry
            5 --> Delete Entry
            6 --> Exit App
        """)
        try:
            choice = input("Kindly enter any choice from the above: ")
            match choice:
                case '1':
                    self.create_diary()
                case '2':
                    self.create_entry()
                case '3':
                    self.find_entry_by()
                case '4':
                    self.update_entry()
                case '5':
                    self.delete_entry_by()
                case '6':
                    self.exit()
        except ValueError:
            print("That is not a valid choice.")

    def create_diary(self):
        try:
            username = input("Kindly Enter A username Of Your Choice: ")
            password = input("Kindly Enter A passkey Of Your Choice: ")
            self.my_diaries.add(username, password)
            print("Diary Created successfully.\nPLEASE NOTE YOUR DIARY IS LOCKED BY DEFAULT")
        except NullPointerException as e:
            print(e)
        finally:
            self.main_menu()

    def create_entry(self):
        try:
            username = input("Kindly Enter your username: ")
            diary = diaries.find_by(username)
            if diary.is_locked():
                password = input("Diary is locked, enter password to unlock: ")
                diary.unlock_diary(password)
            title = input("Kindly Enter The Title Of The Entry: ")
            body = input("Kindly Enter The Body Of The Entry: ")
            diary.create_entry(title, body)
            print("Entry created successfully.\nYour entry Id is " + entry.entry_id)

        except NotFoundException as e:
            print(f"Error: {e}")
        except LockedStateException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            self.main_menu()

    def update_entry(self):
        entry_id = input("Kindly Enter The Unique Id Of The Entry To Update: ")
        new_title = input("Kindly Enter The New Title Of The Entry: ")
        new_body = input("Kindly Enter The New Body Of The Entry: ")
        try:
            self.my_diary.update_entry(int(entry_id), new_title, new_body)
            print("Entry updated successfully.")
        except Exception as e:
            print(e)
        finally:
            self.main_menu()

    def delete_entry_by(self):
        try:
            entry_id = int(input("Kindly Enter The Unique Id Of The Entry To Delete: "))
            diary.delete_entry_by(entry_id)
            print(f"Entry {entry_id} deleted successfully.")
        except NotFoundException as e:
            print(f"Error: {e}")
        finally:
            self.main_menu()

    def welcome(self):
        print("Welcome To AppByMeDiary\n")
        print("The next page Displays And Help You With Your Choice ?\n")

    def exit(self):
        print("Thank You For Using AppByMeDiary")
        sys.exit(0)

    def find_entry_by(self):
        pass
        

