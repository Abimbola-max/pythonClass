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
        self.size += 1


    def peek(self):
        return self.queue[self.head]







