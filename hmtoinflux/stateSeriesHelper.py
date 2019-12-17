from influxdb import SeriesHelper
from . import InfluxClient, config


class STHStateSeriesHelper(SeriesHelper):
    class Meta:
        client = InfluxClient

        # The series name must be a string. Add dependent fields/tags
        # in curly brackets.
        series_name = 'stateSTH'

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
