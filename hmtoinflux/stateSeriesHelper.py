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
            'CONFIG_PENDING_0',
            'DUTY_CYCLE_0',
            'LOW_BAT_0',
            'OPERATING_VOLTAGE_0',
            'OPERATING_VOLTAGE_STATUS_0',
            'RSSI_DEVICE_0',
            'RSSI_PEER_0',
            'UNREACH_0',
            'UPDATE_PENDING_0',
            'ACTIVE_PROFILE_1',
            'ACTUAL_TEMPERATURE_1',
            'ACTUAL_TEMPERATURE_STATUS_1',
            'BOOST_MODE_1',
            'BOOST_TIME_1',
            'CONTROL_DIFFERENTIAL_TEMPERATURE_1',
            'CONTROL_MODE_1',
            'DURATION_UNIT_1',
            'DURATION_VALUE_1',
            'FROST_PROTECTION_1',
            'HEATING_COOLING_1',
            'HUMIDITY_1',
            'HUMIDITY_STATUS_1',
            'PARTY_MODE_1',
            'PARTY_SET_POINT_TEMPERATURE_1',
            'PARTY_TIME_END_1',
            'PARTY_TIME_START_1',
            'QUICK_VETO_TIME_1',
            'SET_POINT_MODE_1',
            'SET_POINT_TEMPERATURE_1',
            'SWITCH_POINT_OCCURED_1',
            'WINDOW_STATE_1'
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

        bulk_size = config.influx.bulk_size
        autocommit = True


class ETRV2StateSeriesHelper(SeriesHelper):
    class Meta:
        client = InfluxClient

        # The series name must be a string. Add dependent fields/tags
        # in curly brackets.
        series_name = 'stateETRV2'

        device_type = DeviceType.ETRV2.value

        fields = [
            'CONFIG_PENDING_0',
            'DUTY_CYCLE_0',
            'LOW_BAT_0',
            'OPERATING_VOLTAGE_0',
            'OPERATING_VOLTAGE_STATUS_0',
            'RSSI_DEVICE_0',
            'RSSI_PEER_0',
            'UNREACH_0',
            'UPDATE_PENDING_0',
            'ACTIVE_PROFILE_1',
            'ACTUAL_TEMPERATURE_1',
            'ACTUAL_TEMPERATURE_STATUS_1',
            'BOOST_MODE_1',
            'BOOST_TIME_1',
            'CONTROL_DIFFERENTIAL_TEMPERATURE_1',
            'CONTROL_MODE_1',
            'DURATION_UNIT_1',
            'DURATION_VALUE_1',
            'FROST_PROTECTION_1',
            'LEVEL_1',
            'LEVEL_STATUS_1',
            'PARTY_MODE_1',
            'PARTY_SET_POINT_TEMPERATURE_1',
            'PARTY_TIME_END_1',
            'PARTY_TIME_START_1',
            'QUICK_VETO_TIME_1',
            'SET_POINT_MODE_1',
            'SET_POINT_TEMPERATURE_1',
            'SWITCH_POINT_OCCURED_1',
            'VALVE_ADAPTION_1',
            'VALVE_STATE_1',
            'WINDOW_STATE_1'
        ]

        tags = ['DEVICE_NAME']

        bulk_size = config.influx.bulk_size
        autocommit = True


class FALMOTC12StateSeriesHelper(SeriesHelper):
    class Meta:
        client = InfluxClient

        # The series name must be a string. Add dependent fields/tags
        # in curly brackets.
        series_name = 'stateFALMOTC12'

        device_type = DeviceType.FALMOTC12.value

        fields = [
            'CONFIG_PENDING_0',
            'DATE_TIME_UNKNOWN_0',
            'DUTY_CYCLE_0',
            'HEATING_COOLING_0',
            'HUMIDITY_ALARM_0',
            'OPERATING_VOLTAGE_0',
            'OPERATING_VOLTAGE_STATUS_0',
            'RSSI_DEVICE_0',
            'RSSI_PEER_0',
            'TEMPERATURE_LIMITER_0',
            'UNREACH_0',
            'UPDATE_PENDING_0',
            'DEW_POINT_ALARM_1',
            'EMERGENCY_OPERATION_1',
            'EXTERNAL_CLOCK_1',
            'FROST_PROTECTION_1',
            'HUMIDITY_LIMITER_1',
            'LEVEL_1',
            'LEVEL_STATUS_1',
            'VALVE_STATE_1',
            'DEW_POINT_ALARM_2',
            'EMERGENCY_OPERATION_2',
            'EXTERNAL_CLOCK_2',
            'FROST_PROTECTION_2',
            'HUMIDITY_LIMITER_2',
            'LEVEL_2',
            'LEVEL_STATUS_2',
            'VALVE_STATE_2',
            'DEW_POINT_ALARM_3',
            'EMERGENCY_OPERATION_3',
            'EXTERNAL_CLOCK_3',
            'FROST_PROTECTION_3',
            'HUMIDITY_LIMITER_3',
            'LEVEL_3',
            'LEVEL_STATUS_3',
            'VALVE_STATE_3',
            'DEW_POINT_ALARM_4',
            'EMERGENCY_OPERATION_4',
            'EXTERNAL_CLOCK_4',
            'FROST_PROTECTION_4',
            'HUMIDITY_LIMITER_4',
            'LEVEL_4',
            'LEVEL_STATUS_4',
            'VALVE_STATE_4',
            'DEW_POINT_ALARM_5',
            'EMERGENCY_OPERATION_5',
            'EXTERNAL_CLOCK_5',
            'FROST_PROTECTION_5',
            'HUMIDITY_LIMITER_5',
            'LEVEL_5',
            'LEVEL_STATUS_5',
            'VALVE_STATE_5',
            'DEW_POINT_ALARM_6',
            'EMERGENCY_OPERATION_6',
            'EXTERNAL_CLOCK_6',
            'FROST_PROTECTION_6',
            'HUMIDITY_LIMITER_6',
            'LEVEL_6',
            'LEVEL_STATUS_6',
            'VALVE_STATE_6',
            'DEW_POINT_ALARM_7',
            'EMERGENCY_OPERATION_7',
            'EXTERNAL_CLOCK_7',
            'FROST_PROTECTION_7',
            'HUMIDITY_LIMITER_7',
            'LEVEL_7',
            'LEVEL_STATUS_7',
            'VALVE_STATE_7',
            'DEW_POINT_ALARM_8',
            'EMERGENCY_OPERATION_8',
            'EXTERNAL_CLOCK_8',
            'FROST_PROTECTION_8',
            'HUMIDITY_LIMITER_8',
            'LEVEL_8',
            'LEVEL_STATUS_8',
            'VALVE_STATE_8',
            'DEW_POINT_ALARM_9',
            'EMERGENCY_OPERATION_9',
            'EXTERNAL_CLOCK_9',
            'FROST_PROTECTION_9',
            'HUMIDITY_LIMITER_9',
            'LEVEL_9',
            'LEVEL_STATUS_9',
            'VALVE_STATE_9',
            'DEW_POINT_ALARM_10',
            'EMERGENCY_OPERATION_10',
            'EXTERNAL_CLOCK_10',
            'FROST_PROTECTION_10',
            'HUMIDITY_LIMITER_10',
            'LEVEL_10',
            'LEVEL_STATUS_10',
            'VALVE_STATE_10',
            'DEW_POINT_ALARM_11',
            'EMERGENCY_OPERATION_11',
            'EXTERNAL_CLOCK_11',
            'FROST_PROTECTION_11',
            'HUMIDITY_LIMITER_11',
            'LEVEL_11',
            'LEVEL_STATUS_11',
            'VALVE_STATE_11',
            'DEW_POINT_ALARM_12',
            'EMERGENCY_OPERATION_12',
            'EXTERNAL_CLOCK_12',
            'FROST_PROTECTION_12',
            'HUMIDITY_LIMITER_12',
            'LEVEL_12',
            'LEVEL_STATUS_12',
            'VALVE_STATE_12',
        ]

        tags = ['DEVICE_NAME']

        bulk_size = config.influx.bulk_size
        autocommit = True


class ESTXWMStateSeriesHelper(SeriesHelper):
    class Meta:
        client = InfluxClient

        # The series name must be a string. Add dependent fields/tags
        # in curly brackets.
        series_name = 'stateESTXWM'

        device_type = DeviceType.ESTXWM.value

        fields = [
            'UNREACH_0',
            'STICKY_UNREACH_0',
            'CONFIG_PENDING_0',
            'LOWBAT_0',
            'RSSI_DEVICE_0',
            'RSSI_PEER_0',
            'DEVICE_IN_BOOTLOADER_0',
            'UPDATE_PENDING_0',
            'GAS_ENERGY_COUNTER_1',
            'GAS_POWER_1',
            'ENERGY_COUNTER_1',
            'POWER_1',
        ]

        tags = ['DEVICE_NAME']

        bulk_size = config.influx.bulk_size
        autocommit = True
