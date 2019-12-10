class Room:
    def __init__(self, name, ise_id, channels):
        self.name = name
        self.ise_id = ise_id
        self.channels = channels

    def get_name(self):
        return self.name

    def get_ise_id(self):
        return self.ise_id

    def get_channels(self):
        return self.channels

    def is_id_in_channels(self, ise_id):
        if ise_id in self.channels:
            return True
        else:
            return False
