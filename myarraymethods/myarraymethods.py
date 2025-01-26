class MyArrayMethod:

    def __init__(self, size):
        self.size = 0
        self.capacity = size
        self.array = [None] * size

    def is_empty(self):
        return self.size == 0

    def add_element(self, element):
        if self.size < self.capacity:
            self.array[self.size] = element
            self.size += 1
        else:
            return "full"


    def extend_element(self, elements):
        for count in elements:
            if self.size < self.capacity:
                self.array[self.size] = count
                self.size += 1
            else:
                return "full"

    def insert_index(self, element, index):
        for count in range(self.size, index, -1):
            self.array[count] = self.array[count - 1]

        self.array[index] = element
        self.size += 1
        return "Element inserted"

    def get_index_of_an_element(self, element):
        for index_counter in range(self.size):
            if self.array[index_counter] == element:
                return index_counter
        return -1

    def len(self):
        return self.size

    def remove_element(self, element):
        for index_counter in range(self.size):
            if self.array[index_counter] == element:
                self.size -= 1
        return "Not Found"

    def clear(self):
        self.array = [None] * self.size
        self.size = 0

    def count(self, element):
        for count in range(self.size, -1, -1):
            if self.array[count] == element:
                return count
        return 0













