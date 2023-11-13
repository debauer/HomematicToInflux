from influxdb import SeriesHelper

from hmtoinflux.data_types import DeviceType


class ESTXWMStateSeriesHelper(SeriesHelper):
    class Meta:
        client = None

        # The series name must be a string. Add dependent fields/tags
        # in curly brackets.
        series_name = "stateESTXWM"

        device_type = DeviceType.ESTXWM.value

        fields = [
            "UNREACH_0",
            "STICKY_UNREACH_0",
            "CONFIG_PENDING_0",
            "LOWBAT_0",
            "RSSI_DEVICE_0",
            "RSSI_PEER_0",
            "DEVICE_IN_BOOTLOADER_0",
            "UPDATE_PENDING_0",
            "GAS_ENERGY_COUNTER_1",
            "GAS_POWER_1",
            "ENERGY_COUNTER_1",
            "POWER_1",
        ]

        tags = ["DEVICE_NAME"]

        bulk_size = 5
        autocommit = True
