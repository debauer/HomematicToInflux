class Device:
    def __init__(self, name, ise_id, address, device_type):
        self.name = name
        self.ise_id = ise_id
        self.address = address
        self.device_type = device_type

    def get_name(self):
        return self.name

    def get_ise_id(self):
        return self.ise_id

    def get_address(self):
        return self.address

    def get_device_type(self):
        return self.device_type

    def is_id_in_channels(self, ise_id):
        if ise_id in self.channels:
            return True
        else:
            return False

    def tostring(self):
        return "device: {0:40} | ise_id: {1:4} | address: {2:14} | device_type: {3:10}".format(self.name, self.ise_id, self.address, self.device_type)
