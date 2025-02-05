from exception import VolumeException, ChannelTypeException, TelevisionStateException


class Television:

    def __init__(self):
        self.volume = 5
        self.channel = 2
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
        if self.is_on:
            raise TelevisionStateException("Television turned off")
        if not self.is_on:
            return self.volume
        if self.volume > 50:
            raise VolumeException("Volume cannot exceed 50")
        self.volume += 5
        return self.volume

    def decrease_volume(self):
        if self.is_on:
            raise TelevisionStateException("Television turned off")
        if self.volume <= 0:
            raise VolumeException("Your tv is currently mute")
        self.volume -= 5
        return self.volume

    def decrease_channel(self):
        if self.channel < 2:
            raise ChannelTypeException("Channel cannot be below 1")
        self.channel -= 2
        return self.channel

    def increase_channel(self):
        if self.is_on:
            raise TelevisionStateException("Television turned off")
        self.channel += 2
        return self.channel

    def set_channel(self, channel_button):
        if self.is_on:
            raise TelevisionStateException("Television turned off")
        if channel_button > 50 or channel_button < 2 and channel_button % 2 != 0:
            raise ChannelTypeException("Channel must be between 2 and 50")
        self.channel = channel_button



