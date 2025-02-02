class Diaries:

    def __init__(self):
        self.diaries = []

    def add(self, username, password):
        self.diaries.append((username, password))

    def get_number_of_diary(self):
        return len(self.diaries)

    def find_by_username(self, username):
        for diary in self.diaries:
            if diary.getUsername() == username:
                return diary



