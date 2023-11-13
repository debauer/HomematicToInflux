from __future__ import annotations

import json
from socket import gethostname
from typing import Any, TypedDict

from overrides import EnforceOverrides


class Measurement(TypedDict):
    measurement: str
    tags: dict[str, str | int]
    fields: dict[str, str | int | float]


class Datapoint(EnforceOverrides):
    def __init__(
        self,
    ) -> None:
        self.point: Measurement = {
            "measurement": "",
            "tags": {"host": gethostname()},
            "fields": {},
        }

    def set_tag(self, tag: str, data: str | int) -> None:
        self.point["tags"][tag] = data

    def set_tags(self, tags: dict[str, str | int]) -> None:
        self.point["tags"] = {**self.point["tags"], **tags}

    # technically we could use isinstance here, but it is more like speaking this way
    # pylint: disable=unidiomatic-typecheck
    def check_type(self, data: Any, expected_type: Any, field_name: str) -> Any:
        if type(data) is not expected_type and (
            # a conversion of ints to float is okay here and we do not need a warning about it
            # this condition is, De Morgan on: not ( type(data) is int and t is float )
            type(data) is not int
            or expected_type is not float
        ):
            print(
                f"data is not an {expected_type.__name__}, type(data): {type(data)}, "
                f"{expected_type.__name__}(data): {expected_type(data)}, "
                f"data: {data}, field: {field_name}",
                f"set_{expected_type.__name__}_field",
            )
        return expected_type(data)

    def set_int_field(self, field: str, data: int) -> None:
        self.point["fields"][field] = self.check_type(data, int, field)

    def set_float_field(self, field: str, data: float) -> None:
        self.point["fields"][field] = self.check_type(data, float, field)

    def set_str_field(self, field: str, data: str) -> None:
        self.point["fields"][field] = self.check_type(data, str, field)

    def set_fields(self, fields: dict[str, str | int | float]) -> None:
        self.point["fields"] = fields

    def __str__(self) -> str:
        return str(self.point)

    def get_point(self) -> str:
        return json.dumps(self.point)


class CameraDataPoint(Datapoint):
    def __init__(self, camera_name: str, group: str) -> None:
        super().__init__()
        self.set_tag("name", str(camera_name))
        self.set_tag("group", group)
