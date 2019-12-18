import inspect
import sys

from hm.valueType import ValueType
from hm.deviceType import DeviceType
from . import stateSeriesHelper
from .stateSeriesHelper import STHStateSeriesHelper, STHOStateSeriesHelper, SWDOStateSeriesHelper, PSMStateSeriesHelper


def format_wrapper(obj, name):
    datapoint = obj.get_datapoint_by_name(name)
    if not datapoint:
        print("[ERROR]["+obj.get_name()+"] no datapoint for state name", name)
        return 0
    type = int(obj.get_datapoint_by_name(name)['valuetype'])
    value = obj.get_datapoint_by_name(name)['value']
    if type == ValueType.ivtInteger.value:
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
    def __init__(self, stateList, deviceList, roomList):
        self.stateList = stateList
        self.deviceList = deviceList
        self.roomList = roomList

    def write_state_data(self):
        func = {}
        for c in inspect.getmembers(stateSeriesHelper, inspect.isclass):
            className = c[0]
            if "StateSeriesHelper" in className:
                stateSeriesHelperClass = getattr(stateSeriesHelper, className)
                func[stateSeriesHelperClass.Meta.device_type] = stateSeriesHelperClass
        for state in self.stateList.states:
            if self.deviceList.get_device_by_name(state.get_name()) is not None:
                deviceType = self.deviceList.get_device_by_name(state.get_name()).get_device_type()
                if deviceType in func:
                    buildCall(func[deviceType], state)
