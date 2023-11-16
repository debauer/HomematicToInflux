from __future__ import annotations

from typing import Any

from hmtoinflux.data_types.device import Device as Device
from hmtoinflux.data_types.room import Room as Room
from hmtoinflux.data_types.state import State as State


InfluxDatapoint = dict[str, Any]
