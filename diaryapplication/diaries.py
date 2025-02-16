from diaryapplication.diary import Diary
from diaryapplication.exception import NotFoundException


class Diaries:

    def __init__(self):
        self.diaries = []

    def add(self, username, password):
        new_diary = Diary(username, password)
        self.diaries.append(new_diary)
        return new_diary

    def get_number_of_diaries(self):
        return len(self.diaries)

    def find_by(self, username):
        for diary in self.diaries:
            if diary.username == username:
                return diary
        raise NotFoundException("Diary not found")

