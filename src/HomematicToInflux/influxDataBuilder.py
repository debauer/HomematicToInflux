import inspect

from influxdb import InfluxDBClient

from HomematicToInflux.data_types import ValueType
from HomematicToInflux.lists import StateList, DeviceList, RoomList
from HomematicToInflux.series_helper.mapping import helper_mapping


def format_wrapper(obj, name):
    datapoint = obj.get_datapoint_by_name(name)
    if not datapoint:
        print("[ERROR]["+obj.get_name()+"] no datapoint for state name", name)
        return 0
    type = int(obj.get_datapoint_by_name(name)['valuetype'])
    value = obj.get_datapoint_by_name(name)['value']
    if type == ValueType.ivtInteger.value or type == ValueType.ivtRSSI.value:
        #if type == ValueType.ivtRSSI.value:
        #    print("rssi" + value)
        if value == '':
            return 0
        return int(value)
    elif type == ValueType.ivtFloat.value:
        if value == '':
            return 0.0
        return float(value)
    else:
        return value


def buildArguments(helper, state):
    name = state.get_name()
    fields = helper.Meta.fields
    args = {'DEVICE_NAME': name}
    for t in fields:
        args[t] = format_wrapper(state, t)
    return args


def buildCall(func, state):
    func(**buildArguments(func, state))


class InfluxDataBuilder:
    def __init__(self, states: StateList, devices: DeviceList, rooms: RoomList):
        self.states = states
        self.devices = devices
        self.rooms = rooms
        self.client = InfluxDBClient('localhost', 8086, 'root', 'root', 'homematicToInflux')

    def update(self):
        for state in self.states.states:
            if self.devices.get_device_by_name(state.get_name()) is not None:
                deviceType = self.devices.get_device_by_name(state.get_name()).get_device_type()
                if deviceType in helper_mapping:
                    helper_mapping[deviceType](state)
