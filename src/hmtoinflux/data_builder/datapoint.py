from dataclasses import dataclass
from dataclasses import field
from typing import Union

from hmtoinflux.config_wrapper.types import InfluxDB
from hmtoinflux.data_types import State, Device


@dataclass
class InfluxPoint:
    state: State
    config: InfluxDB
    device: Device

    device_type: str = field(init=False)
    datapoints: list[dict[str, any]] = field(init=False)

    def __str__(self) -> str:
        return f"{'/'.join(self.mqtt_topic)}, {self.measurement=}"

    @staticmethod
    def _parse_value(value: str) -> Union[str, int, float]:
        try:
            return float(value)
        except ValueError:
            if value.lower() == 'false':
                return False
            if value.lower() == 'true':
                return True
            print("fuck is string:", value)
            return value

    def __post_init__(self) -> None:
        self.datapoints = []
        fields = {p["name"]: self._parse_value(p["value"]) for p in self.state.datapoints if p["value"] != ""}
        if fields:
            self._add_datapoint(fields)

    def _add_datapoint(self, fields):
        self.datapoints.append(
            {
                "measurement": self.device.device_type,
                "tags": {
                    "device_name": self.device.name,
                    "device_type": self.device.device_type,
                },
                "fields": fields,
            }
        )
