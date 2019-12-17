from hm.valueType import ValueType
from hm.deviceType import DeviceType
from .stateSeriesHelper import STHStateSeriesHelper


def format_wrapper(obj, name):
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


class InfluxDataBuilder:
    def __init__(self, stateList, deviceList, roomList):
        self.stateList = stateList
        self.deviceList = deviceList
        self.roomList = roomList

    def write_state_data(self):
        for state in self.stateList.states:
            if self.deviceList.get_device_by_name(state.get_name()) is not None:
                if self.deviceList.get_device_by_name(state.get_name()).get_device_type() == DeviceType.STH.value:
                    STHStateSeriesHelper(
                        DEVICE_NAME=state.get_name(),
                        CONFIG_PENDING=format_wrapper(state, 'CONFIG_PENDING'),
                        DUTY_CYCLE=format_wrapper(state, 'DUTY_CYCLE'),
                        LOW_BAT=format_wrapper(state, 'LOW_BAT'),
                        OPERATING_VOLTAGE=format_wrapper(state, 'OPERATING_VOLTAGE'),
                        OPERATING_VOLTAGE_STATUS=format_wrapper(state, 'OPERATING_VOLTAGE_STATUS'),
                        RSSI_DEVICE=format_wrapper(state, 'RSSI_DEVICE'),
                        RSSI_PEER=format_wrapper(state, 'RSSI_PEER'),
                        UNREACH=format_wrapper(state, 'UNREACH'),
                        UPDATE_PENDING=format_wrapper(state, 'UPDATE_PENDING'),
                        ACTIVE_PROFILE=format_wrapper(state, 'ACTIVE_PROFILE'),
                        ACTUAL_TEMPERATURE=format_wrapper(state, 'ACTUAL_TEMPERATURE'),
                        ACTUAL_TEMPERATURE_STATUS=format_wrapper(state, 'ACTUAL_TEMPERATURE_STATUS'),
                        BOOST_MODE=format_wrapper(state, 'BOOST_MODE'),
                        BOOST_TIME=format_wrapper(state, 'BOOST_TIME'),
                        CONTROL_DIFFERENTIAL_TEMPERATURE=format_wrapper(state, 'CONTROL_DIFFERENTIAL_TEMPERATURE'),
                        CONTROL_MODE=format_wrapper(state, 'CONTROL_MODE'),
                        DURATION_UNIT=format_wrapper(state, 'DURATION_UNIT'),
                        DURATION_VALUE=format_wrapper(state, 'DURATION_VALUE'),
                        FROST_PROTECTION=format_wrapper(state, 'FROST_PROTECTION'),
                        HEATING_COOLING=format_wrapper(state, 'HEATING_COOLING'),
                        HUMIDITY=format_wrapper(state, 'HUMIDITY'),
                        HUMIDITY_STATUS=format_wrapper(state, 'HUMIDITY_STATUS'),
                        PARTY_MODE=format_wrapper(state, 'PARTY_MODE'),
                        PARTY_SET_POINT_TEMPERATURE=format_wrapper(state, 'PARTY_SET_POINT_TEMPERATURE'),
                        PARTY_TIME_END=format_wrapper(state, 'PARTY_TIME_END'),
                        PARTY_TIME_START=format_wrapper(state, 'PARTY_TIME_START'),
                        QUICK_VETO_TIME=format_wrapper(state, 'QUICK_VETO_TIME'),
                        SET_POINT_MODE=format_wrapper(state, 'SET_POINT_MODE'),
                        SET_POINT_TEMPERATURE=format_wrapper(state, 'SET_POINT_TEMPERATURE'),
                        SWITCH_POINT_OCCURED=format_wrapper(state, 'SWITCH_POINT_OCCURED'),
                        WINDOW_STATE=format_wrapper(state, 'WINDOW_STATE')
                    )
