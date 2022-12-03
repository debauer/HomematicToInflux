from influxdb import SeriesHelper

from HomematicToInflux.data_types import DeviceType


class STHOStateSeriesHelper(SeriesHelper):
    class Meta:
        client = None

        # The series name must be a string. Add dependent fields/tags
        # in curly brackets.
        series_name = 'stateSTHO'

        device_type = DeviceType.STHO.value

        fields = [
            'CONFIG_PENDING_0',
            'DUTY_CYCLE_0',
            'ERROR_CODE_0',
            'LOW_BAT_0',
            'OPERATING_VOLTAGE_0',
            'OPERATING_VOLTAGE_STATUS_0',
            'RSSI_DEVICE_0',
            'RSSI_PEER_0',
            'TEMPERATURE_OUT_OF_RANGE_0',
            'UNREACH_0',
            'UPDATE_PENDING_0',
            'ACTUAL_TEMPERATURE_1',
            'ACTUAL_TEMPERATURE_STATUS_1',
            'HUMIDITY_1',
            'HUMIDITY_STATUS_1'
        ]

        tags = ['DEVICE_NAME']

        bulk_size = 5
        autocommit = True
