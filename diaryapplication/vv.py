import datetime

class Movie:
    def __init__(self, title):
        self.__title = title
        self.ratings = []
        self.added_on = datetime.datetime.now()

    @property
    def title(self):
        return self.__title

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)
        else:
            print("Invalid rating. Rating must be between 1 and 5.")

    def get_average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

    def __str__(self):
        return f"Title: {self.title}, Added on: {self.added_on.strftime('%Y-%m-%d %H:%M:%S')}, Average Rating: {self.get_average_rating():.2f}"

class MovieApp:
    def __init__(self):
        self.movies = {}

    def add_movie(self, title):
        if title in self.movies:
            print(f"Movie '{title}' already exists.")
            return
        movie = Movie(title)
        self.movies[title] = movie
        print(f"Movie '{title}' added on {movie.added_on.strftime('%Y-%m-%d %H:%M:%S')}.")

    def rate_movie(self, title, rating):
        if title not in self.movies:
            print(f"Movie '{title}' not found.")
            return
        self.movies[title].add_rating(rating)
        print(f"Rating {rating} added for movie '{title}'.")

    def get_average_rating(self, title):
        if title not in self.movies:
            print(f"Movie '{title}' not found.")
            return 0
        return self.movies[title].get_average_rating()

    def get_average_ratings_all_movies(self):
        if not self.movies:
            return 0
        total_average = sum(movie.get_average_rating() for movie in self.movies.values())
        return total_average / len(self.movies)

    def display_movies(self):
        if not self.movies:
            print("No movies in the app yet.")
            return
        print("\n--- Movies in the App ---")
        for movie in self.movies.values():
            print(movie)
        print("-------------------------\n")

def main():
    movie_app = MovieApp()

    while True:
        print("\nMovie Rating Application")
        print("1. Add a movie")
        print("2. Rate a movie")
        print("3. Get average rating for a movie")
        print("4. Get average ratings of all movies")
        print("5. List all movies")
        print("6. Exit the application")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the title of the movie to add: ")
            movie_app.add_movie(title)
        elif choice == '2':
            title = input("Enter the title of the movie to rate: ")
            try:
                rating = int(input("Enter your rating (1-5): "))
                movie_app.rate_movie(title, rating)
            except ValueError:
                print("Invalid input. Please enter a number for the rating.")
        elif choice == '3':
            title = input("Enter the title of the movie to get the average rating for: ")
            average_rating = movie_app.get_average_rating(title)
            print(f"Average rating for '{title}': {average_rating:.2f}")
        elif choice == '4':
            average_all = movie_app.get_average_ratings_all_movies()
            print(f"Average rating of all movies in the app: {average_all:.2f}")
        elif choice == '5':
            movie_app.display_movies()
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



class Movie:
    def __init__(self, title):
        self.title = title
        self.ratings = []
        self.date_time = datetime.datetime.now()

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)
        else:
            raise InvalidRatingException("Rating must be between 1 and 5.")

    def get_average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

    def __str__(self):
        return f"Title: {self.title}, Added on: {self.date_time.strftime('%Y-%m-%d %H:%M')}, Average Rating: {self.get_average_rating():.2f}"

class MovieAlreadyExistException(Exception):
    pass

class MovieNotFoundException(Exception):
    pass

class InvalidRatingException(Exception):
    pass

class NullException(Exception):
    pass

class Validator:
    @staticmethod
    def validate_title(title):
        if not title:
            raise NullException("Movie title cannot be empty.")

    @staticmethod
    def validate_rating(rating):
        if not isinstance(rating, int):
            raise InvalidRatingException("Rating must be an integer.")
        if not (1 <= rating <= 5):
            raise InvalidRatingException("Rating must be between 1 and 5.")

class Movies:
    def __init__(self):
        self.movies = {}

    def add_movie(self, title):
        if title in self.movies:
            raise MovieAlreadyExistException(f"Movie '{title}' already exists.")

        movie = Movie(title)
        self.movies[title] = movie
        print(f"Movie '{title}' added on {movie.date_time.strftime('%Y-%m-%d %H:%M')}.")

    def rate_movie(self, title, rating):
        if title not in self.movies:
            raise MovieNotFoundException(f"Movie '{title}' not found.")
        self.movies[title].add_rating(rating)
        print(f"Rating {rating} added for movie '{title}'.")

    def get_average_ratings(self, title):
        if title not in self.movies:
            raise MovieNotFoundException(f"Movie '{title}' not found.")
        return self.movies[title].get_average_rating()

    def view_average_ratings(self):
        if not self.movies:
            print("No movies in the system yet.")
            return
        print("\n--- Average Ratings ---")
        for title, movie in self.movies.items():
            print(f"{title}: {movie.get_average_rating():.2f}")
        print("-----------------------\n")

    def display_movies(self):
        if not self.movies:
            print("No movies in the system yet.")
            return
        print("\n--- Movies in the System ---")
        for title, movie in self.movies.items():
            print(movie)
        print("---------------------------\n")

class MovieApp:
    def __init__(self):
        self.movies_instance = Movies()

    def main_menu(self):
        while True:
            print("\nMovie Rating Application")
            print("1. Add a movie")
            print("2. Rate a movie")
            print("3. View average ratings")
            print("4. List all movies")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_a_movie()
            elif choice == "2":
                self.rate_a_movie()
            elif choice == "3":
                self.movies_instance.view_average_ratings()
            elif choice == "4":
                self.movies_instance.display_movies()
            elif choice == "5":
                print("Exiting application.")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_a_movie(self):
        try:
            title = input("Enter movie title: ").lower()
            Validator.validate_title(title)
            self.movies_instance.add_movie(title)
        except NullException as e:
            print(f"Error: {e}")
        except MovieAlreadyExistException as e:
            print(f"Error: {e}")

    def rate_a_movie(self):
        try:
            title = input("Enter movie title to rate: ").lower()
            Validator.validate_title(title)
            rating = int(input("Enter movie rating (1-5): "))
            Validator.validate_rating(rating)
            self.movies_instance.rate_movie(title, rating)
            print(f"Movie '{title}' rated: {rating}")
        except NullException as e:
            print(f"Error: {e}")
        except InvalidRatingException as e:
            print(f"Error: {e}")
        except MovieNotFoundException as e:
            print(f"Error: {e}")
        except ValueError:
            print("Error: Rating must be an integer.")

if __name__ == "__main__":
    app = MovieApp()
    app.main_menu()