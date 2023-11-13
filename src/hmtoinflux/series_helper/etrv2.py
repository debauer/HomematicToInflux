from influxdb import SeriesHelper

from hmtoinflux.data_types import DeviceType


class ETRV2StateSeriesHelper(SeriesHelper):
    class Meta:
        client = None

        # The series name must be a string. Add dependent fields/tags
        # in curly brackets.
        series_name = "stateETRV2"

        device_type = DeviceType.ETRV2.value

        fields = [
            "CONFIG_PENDING_0",
            "DUTY_CYCLE_0",
            "LOW_BAT_0",
            "OPERATING_VOLTAGE_0",
            "OPERATING_VOLTAGE_STATUS_0",
            "RSSI_DEVICE_0",
            "RSSI_PEER_0",
            "UNREACH_0",
            "UPDATE_PENDING_0",
            "ACTIVE_PROFILE_1",
            "ACTUAL_TEMPERATURE_1",
            "ACTUAL_TEMPERATURE_STATUS_1",
            "BOOST_MODE_1",
            "BOOST_TIME_1",
            "CONTROL_DIFFERENTIAL_TEMPERATURE_1",
            "CONTROL_MODE_1",
            "DURATION_UNIT_1",
            "DURATION_VALUE_1",
            "FROST_PROTECTION_1",
            "LEVEL_1",
            "LEVEL_STATUS_1",
            "PARTY_MODE_1",
            "PARTY_SET_POINT_TEMPERATURE_1",
            "PARTY_TIME_END_1",
            "PARTY_TIME_START_1",
            "QUICK_VETO_TIME_1",
            "SET_POINT_MODE_1",
            "SET_POINT_TEMPERATURE_1",
            "SWITCH_POINT_OCCURED_1",
            "VALVE_ADAPTION_1",
            "VALVE_STATE_1",
            "WINDOW_STATE_1",
        ]

        tags = ["DEVICE_NAME"]

        bulk_size = 5
        autocommit = True
