class MyMap:

    def __init__(self, data = None):
        self.values = {}
        self.keys = []
        self.data = data

    def is_empty(self):
        if not self.keys:
            return True
        else:
            return False

    def add(self, key, value):




