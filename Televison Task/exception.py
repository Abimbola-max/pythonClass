class VolumeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ChannelTypeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)