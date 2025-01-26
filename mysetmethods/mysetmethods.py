from myarraymethods import MyArrayMethod


class MySet:

    def __init__(self, size):
        self.array_method = MyArrayMethod(size)

    def is_empty(self):
        return self.array_method.is_empty()

    def add_element(self, element):
        self.array_method.add_element(element)

    def len(self):
        return self.array_method.len()

    def remove_element(self, element):
        self.array_method.remove_element(element)

    def insert_element_at(self, element, index):
        return self.array_method.insert_index(element, index)

    def get_index_of(self, element):
        return self.array_method.get_index_of_an_element(element)

    def clear(self):
         self.array_method.clear()










