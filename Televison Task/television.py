class Television:

    def __init__(self):
        self.volume = 5
        self.channel = 1
        self.is_on = False
        self.mute = 0

    def is_tv_on(self):
        return self.is_on

    def turn_off(self):
        return self.is_on

    def turn_on(self):
        self.is_on = True
        return self.is_on

    def increase_volume(self):
        if not self.is_on:
            return self.volume
        if self.volume > 50:
            raise ValueError("Volume cannot exceed 50")
        if self.volume == 0:
            return self.mute
        self.volume += 5
        return self.volume

    def decrease_volume(self):
        if self.volume <= 0:
            return self.mute
        self.volume -= 5
        return self.volume


