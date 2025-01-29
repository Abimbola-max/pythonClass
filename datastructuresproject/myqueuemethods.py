class MyQueue:

    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.queue = [None] * capacity
        self.tail = 0
        self.head = 0

    def is_empty(self):
        return self.size == 0

    def add(self, element):
        self.queue[self.tail] = element
        self.tail += 1
        self.size += 1

    def peek(self):
        return self.queue[self.head]

    def dequeue(self, element):
        removed_element = self.queue.element
        for index_counter in range(self.queue.getSize() - 1):
            self.queue.elements[index_counter] = self.queue.elements[index_counter + 1]
        self.queue.elements[self.queue.getSize() - 1] = None
        self.queue.size -= 1
        return removed_element

    def find_index_of(self, element):
        for index, values in enumerate(self.queue):
            if values == element:
                return index

        return -1











