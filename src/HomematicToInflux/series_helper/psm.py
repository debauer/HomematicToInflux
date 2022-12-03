from influxdb import SeriesHelper

from HomematicToInflux.types import DeviceType

# Schalt-Mess-Steckdose
class PSMStateSeriesHelper(SeriesHelper):
    class Meta:
        client = None

        # The series name must be a string. Add dependent fields/tags
        # in curly brackets.
        series_name = 'statePSM'

        device_type = DeviceType.PSM.value

        fields = [
            'CONFIG_PENDING_0',
            'DUTY_CYCLE_0',
            'ERROR_CODE_0',
            'OPERATING_VOLTAGE_0',
            'OPERATING_VOLTAGE_STATUS_0',
            'RSSI_DEVICE_0',
            'RSSI_PEER_0',
            'UNREACH_0',
            'UPDATE_PENDING_0',
            'ACTUAL_TEMPERATURE_0',
            'ACTUAL_TEMPERATURE_STATUS_0',
            'ERROR_OVERHEAT_0',
            'PRESS_LONG_1',
            'PRESS_SHORT_1',
            'PROCESS_2',
            'SECTION_2',
            'SECTION_STATUS_2',
            'STATE_2',
            'PROCESS_3',
            'SECTION_3',
            'SECTION_STATUS_3',
            'STATE_3',
            'PROCESS_4',
            'SECTION_4',
            'SECTION_STATUS_4',
            'STATE_4',
            'PROCESS_5',
            'SECTION_5',
            'SECTION_STATUS_5',
            'CURRENT_6',
            'CURRENT_STATUS_6',
            'ENERGY_COUNTER_6',
            'ENERGY_COUNTER_OVERFLOW_6',
            'FREQUENCY_6',
            'FREQUENCY_STATUS_6',
            'POWER_6',
            'POWER_STATUS_6',
            'VOLTAGE_6',
            'VOLTAGE_STATUS_6'
        ]

        tags = ['DEVICE_NAME']

        bulk_size = 5
        autocommit = True

