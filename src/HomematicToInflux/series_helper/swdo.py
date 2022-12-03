from influxdb import SeriesHelper

from HomematicToInflux.types import DeviceType
class SWDOStateSeriesHelper(SeriesHelper):
    class Meta:
        client = None

        # The series name must be a string. Add dependent fields/tags
        # in curly brackets.
        series_name = 'stateSWDO'

        device_type = DeviceType.SWDO.value

        fields = [
            'CONFIG_PENDING_0',
            'DUTY_CYCLE_0',
            'ERROR_CODE_0',
            'LOW_BAT_0',
            'OPERATING_VOLTAGE_0',
            'OPERATING_VOLTAGE_STATUS_0',
            'RSSI_DEVICE_0',
            'RSSI_PEER_0',
            'SABOTAGE_0',
            'UNREACH_0',
            'UPDATE_PENDING_0',
            'STATE_1'
        ]

        tags = ['DEVICE_NAME']

        bulk_size = 5
        autocommit = True



