
class State:
    def __init__(self, name, ise_id, datapoints):
        self.name = name
        self.ise_id = ise_id
        self.datapoints = datapoints

    def __str__(self):
        return self.tostring()

    def get_name(self):
        return self.name

    def get_ise_id(self):
        return self.ise_id

    def get_datapoints(self):
        return self.datapoints

    def get_datapoint_by_name(self, name):
        for datapoint in self.datapoints:
            if 'name' in datapoint and datapoint['name'] == name:
                return datapoint

    def is_id_in_datapoints(self, ise_id):
        if ise_id in self.datapoints:
            return True
        else:
            return False

    def tostring(self):
        return "state: {0:40} | ise_id: {1:4} | datapoints: {2:14}".format(self.name, self.ise_id,
                                                                           str(len(self.datapoints)))
