from influxdb import SeriesHelper
from hm.deviceType import DeviceType
from . import InfluxClient, config


class STHStateSeriesHelper(SeriesHelper):
    class Meta:
        client = InfluxClient

        # The series name must be a string. Add dependent fields/tags
        # in curly brackets.
        series_name = 'stateSTH'

        device_type = DeviceType.STH.value

        fields = [
            'CONFIG_PENDING',
            'DUTY_CYCLE',
            'LOW_BAT',
            'OPERATING_VOLTAGE',
            'OPERATING_VOLTAGE_STATUS',
            'RSSI_DEVICE',
            'RSSI_PEER',
            'UNREACH',
            'UPDATE_PENDING',
            'ACTIVE_PROFILE',
            'ACTUAL_TEMPERATURE',
            'ACTUAL_TEMPERATURE_STATUS',
            'BOOST_MODE',
            'BOOST_TIME',
            'CONTROL_DIFFERENTIAL_TEMPERATURE',
            'CONTROL_MODE',
            'DURATION_UNIT',
            'DURATION_VALUE',
            'FROST_PROTECTION',
            'HEATING_COOLING',
            'HUMIDITY',
            'HUMIDITY_STATUS',
            'PARTY_MODE',
            'PARTY_SET_POINT_TEMPERATURE',
            'PARTY_TIME_END',
            'PARTY_TIME_START',
            'QUICK_VETO_TIME',
            'SET_POINT_MODE',
            'SET_POINT_TEMPERATURE',
            'SWITCH_POINT_OCCURED',
            'WINDOW_STATE'
        ]

        tags = ['DEVICE_NAME']

        bulk_size = config.influx.bulk_size
        autocommit = True


class STHOStateSeriesHelper(SeriesHelper):
    class Meta:
        client = InfluxClient

        # The series name must be a string. Add dependent fields/tags
        # in curly brackets.
        series_name = 'stateSTHO'

        device_type = DeviceType.STHO.value

        fields = [
            'CONFIG_PENDING',
            'DUTY_CYCLE',
            'ERROR_CODE',
            'LOW_BAT',
            'OPERATING_VOLTAGE',
            'OPERATING_VOLTAGE_STATUS',
            'RSSI_DEVICE',
            'RSSI_PEER',
            'TEMPERATURE_OUT_OF_RANGE',
            'UNREACH',
            'UPDATE_PENDING',
            'ACTUAL_TEMPERATURE',
            'ACTUAL_TEMPERATURE_STATUS',
            'HUMIDITY',
            'HUMIDITY_STATUS'
        ]

        tags = ['DEVICE_NAME']

        bulk_size = config.influx.bulk_size
        autocommit = True


class SWDOStateSeriesHelper(SeriesHelper):
    class Meta:
        client = InfluxClient

        # The series name must be a string. Add dependent fields/tags
        # in curly brackets.
        series_name = 'stateSWDO'

        device_type = DeviceType.SWDO.value

        fields = [
            'CONFIG_PENDING',
            'DUTY_CYCLE',
            'ERROR_CODE',
            'LOW_BAT',
            'OPERATING_VOLTAGE',
            'OPERATING_VOLTAGE_STATUS',
            'RSSI_DEVICE',
            'RSSI_PEER',
            'SABOTAGE',
            'UNREACH',
            'UPDATE_PENDING',
            'STATE'
        ]

        tags = ['DEVICE_NAME']

        bulk_size = config.influx.bulk_size
        autocommit = True


# Schalt-Mess-Steckdose
class PSMStateSeriesHelper(SeriesHelper):
    class Meta:
        client = InfluxClient

        # The series name must be a string. Add dependent fields/tags
        # in curly brackets.
        series_name = 'statePSM'

        device_type = DeviceType.PSM.value

        fields = [
            'CONFIG_PENDING',
            'DUTY_CYCLE',
            'ERROR_CODE',
            'OPERATING_VOLTAGE',
            'OPERATING_VOLTAGE_STATUS',
            'RSSI_DEVICE',
            'RSSI_PEER',
            'UNREACH',
            'UPDATE_PENDING',
            'ACTUAL_TEMPERATURE',
            'ACTUAL_TEMPERATURE_STATUS',
            'ERROR_OVERHEAT',
            'PRESS_LONG',
            'PRESS_SHORT',
            'CURRENT',
            'CURRENT_STATUS',
            'ENERGY_COUNTER',
            'ENERGY_COUNTER_OVERFLOW',
            'FREQUENCY',
            'FREQUENCY_STATUS',
            'POWER',
            'POWER_STATUS',
            'VOLTAGE',
            'VOLTAGE_STATUS'
        ]

        tags = ['DEVICE_NAME']

        bulk_size = config.influx.bulk_size
        autocommit = True
