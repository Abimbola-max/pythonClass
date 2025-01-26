from myarraymethods import MyArrayMethod


class MySet:

    def __init__(self, size):
        self.array_method = MyArrayMethod(size)

    def is_empty(self):
        return True

    def add_element(self, element):
        self.array_method.add_element(element)





