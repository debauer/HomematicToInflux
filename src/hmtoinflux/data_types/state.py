from __future__ import annotations

from hmtoinflux.data_types import InfluxDatapoint


class State:
    def __init__(
        self,
        name: str,
        ise_id: int,
        datapoints: list[InfluxDatapoint],
    ) -> None:
        self.name = name
        self.ise_id = ise_id
        self.datapoints = datapoints

    def __str__(self) -> str:
        return self.tostring()

    def get_name(self) -> str:
        return self.name

    def get_ise_id(self) -> int:
        return self.ise_id

    def get_datapoints(self) -> list[InfluxDatapoint]:
        return self.datapoints

    def get_datapoint_by_name(self, name: str) -> InfluxDatapoint:
        for datapoint in self.datapoints:
            if "name" in datapoint and datapoint["name"] == name:
                return datapoint
        return {}

    def is_id_in_datapoints(self, ise_id: int) -> bool:
        if ise_id in self.datapoints:
            return True
        return False

    def tostring(self) -> str:
        return f"state: {self.name:40} | ise_id: {self.ise_id:4} | datapoints: {len(self.datapoints)!s:14}"
