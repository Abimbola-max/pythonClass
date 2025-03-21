import sys

from SCMS.exceptions.exception import NullException
from movieRatingApp.exceptions.exception import *
from movieRatingApp.src.movies import Movies
from movieRatingApp.src.validator import Validator


class Main:

    def __init__(self):
        self.movies_app = Movies()

    def main_menu(self):
        print("Welcome to Movie Rating App")
        print("""
                1. Add a movie
                2. Rate a movie
                3. View Average Ratings
                4. Exit
                """)
        choice = input("Enter your choice: ")
        if choice == "1":
            self.add_movie()
        elif choice == "2":
            self.rate_a_movie()
        elif choice == "3":
            self.view_average_ratings()
            self.main_menu()
        elif choice == "4":
            self.exit_app()
        else:
            print("Invalid choice")
            self.main_menu()

    def add_movie(self):
        try:
            title = input("Enter movie title: ").lower()
            Validator.validate_title(title)
            self.movies_app.add_movie(title)
        except NullException as e:
            print(f"Error {e}")
        except MovieAlreadyExistException as e:
            print(f"Error {e}")
        finally:
            self.main_menu()

    def rate_a_movie(self):
        try:
            title = input("Enter movie title: ").lower()
            Validator.validate_title(title)
            rating = int(input("Enter movie rating: "))
            Validator.validate_rating(rating)
            self.movies_app.rate_movie(title, rating)
            print(f"Movie {title} rated: {rating}")
        except NullException as e:
            print(f"Error {e}")
        except InvalidRatingException as e:
            print(f"Error {e}.")
        except MovieNotFoundException as e:
            print(f"Not found")
        finally:
            self.main_menu()

    def view_average_ratings(self):
        try:
            print("""
                1. View average rating on a movie
                2. View average rating on all movie
                3. Go back
            """)
            choice = input("Enter your choice: ")
            if choice == "1":
                title = input("Enter movie title: ")
                Validator.validate_title(title)
                rate = self.movies_app.get_average_ratings(title)
                print(f"Average rating for {title} is: {rate:.2f}")
            elif choice == "2":
                self.movies_app.view_average_ratings()
            elif choice == "3":
                self.main_menu()
            else:
                print("Invalid choice")
                self.view_average_ratings()
        except NullException as e:
            print(f"Error {e}")
        except InvalidRatingException as e:
            print(f"Error {e}.")
        except MovieNotFoundException as e:
            print(f"Not found")


    @staticmethod
    def exit_app():
        print("Thank you for using Movie Rating App")
        sys.exit(0)


if __name__ == "__main__":
    app = Main()
    app.main_menu()