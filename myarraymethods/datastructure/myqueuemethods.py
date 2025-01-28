from datastructure.myarraymethods import MyArrayMethod

class MyQueue:

    def __init__(self, size):
        self.queue = MyArrayMethod(size)

    def is_empty(self):
        return self.queue.is_empty()

    def add(self, element):
        self.queue.add_element(element)






