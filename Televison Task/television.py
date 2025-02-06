from exception import VolumeException, ChannelTypeException, TelevisionStateException


class Television:

    def __init__(self):
        self._volume = 5
        self._channel = 2
        self.is_on = False
        self.mute = 0

    @property
    def volume(self):
        return self._volume

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, channel):
        self._channel = channel

    def is_tv_on(self):
        return self.is_on

    def turn_off(self):
        return self.is_on

    def turn_on(self):
        self.is_on = True
        return self.is_on

    def increase_volume(self):
        if self.is_on == False:
            raise TelevisionStateException("Television is turned off")
        if self._volume > 50:
            raise VolumeException("Volume cannot exceed 50")
        self._volume += 5
        return self._volume

    def decrease_volume(self):
        if self.is_on == False:
            raise TelevisionStateException("Television is turned off")
        if self._volume == 0:
            raise VolumeException("Your tv is currently mute")
        self._volume -= 5
        return self._volume

    def decrease_channel(self):
        if self._channel < 2:
            raise ChannelTypeException("Channel cannot be below 1")
        self._channel -= 2
        return self._channel

    def increase_channel(self):
        if self.is_on == False:
            raise TelevisionStateException("Television is turned off")
        self._channel += 2
        return self._channel

    def set_channel(self, channel_button):
        if self.is_on == False:
            raise TelevisionStateException("Television is turned off")
        if channel_button > 50 or channel_button < 2 and channel_button % 2 != 0:
            raise ChannelTypeException("Channel must be between 2 and 50")
        self._channel = channel_button



