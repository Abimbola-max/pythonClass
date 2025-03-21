from datetime import datetime


class Movie:

    def __init__(self, title):
        self.title = title
        self.date_time = datetime.now()
        self.rating = []

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    def add_rating(self, rating):
        result = self.rating.append(rating)
        return str(result)

    def get_average_rating(self):
        return sum(self.rating) / len(self.rating)

    def __repr__(self):
        return f"Movie Title: {self.title} was added at {self.date_time.strftime("%Y-%M-%D %h:%m")} by {self.get_average_rating():.1f}"