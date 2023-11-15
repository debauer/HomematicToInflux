from influxdb import InfluxDBClient

from hmtoinflux.config_wrapper.wrapper import ConfigWrapper
from hmtoinflux.data_builder.datapoint import InfluxPoint
from hmtoinflux.lists import StateList, DeviceList, RoomList


class InfluxDataBuilder:
    def __init__(self, states: StateList, devices: DeviceList, rooms: RoomList):
        self.states = states
        self.devices = devices
        self.rooms = rooms
        config = ConfigWrapper().influxdb
        self.client = InfluxDBClient(
            config.address, config.port, config.user, config.password, config.database_name
        )
        self.config = config

    def update(self):
        for state in self.states.states:
            if self.devices.get_device_by_name(state.get_name()) is not None:
                device = self.devices.get_device_by_name(
                    state.get_name()
                )
                points = InfluxPoint(state=state, config=self.config, device=device)
                self.client.write_points(points.datapoints)
