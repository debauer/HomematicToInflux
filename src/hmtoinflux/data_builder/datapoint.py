from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import Any

from hmtoinflux.config_wrapper.types import InfluxDB
from hmtoinflux.data_types import Device
from hmtoinflux.data_types import State


@dataclass
class InfluxPoint:
    state: State
    config: InfluxDB
    device: Device

    device_type: str = field(init=False)
    datapoints: list[dict[str, Any]] = field(init=False)

    def __str__(self) -> str:
        return f"{'/'.join(self.device.name)}, {self.device.device_type=}"

    @staticmethod
    def _parse_value(value: str) -> str | (int | float):
        try:
            return float(value)
        except ValueError:
            if value.lower() == "false":
                return False
            if value.lower() == "true":
                return True
            return value

    def __post_init__(self) -> None:
        self.datapoints = []
        fields = {
            p["name"]: self._parse_value(p["value"])
            for p in self.state.datapoints
            if not p["value"]
        }
        if fields:
            self._add_datapoint(fields)

    def _add_datapoint(self, fields: dict[str, Any]) -> None:
        self.datapoints.append(
            {
                "measurement": self.device.device_type,
                "tags": {
                    "device_name": self.device.name,
                    "device_type": self.device.device_type,
                },
                "fields": fields,
            },
        )
