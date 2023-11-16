from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from hmtoinflux.config import CCU
from hmtoinflux.config import INFLUX_DB
from hmtoinflux.config_wrapper.types import HomematicCCU
from hmtoinflux.config_wrapper.types import InfluxDB


@dataclass
class ConfigWrapper:
    influxdb: InfluxDB = field(init=False)
    ccu: HomematicCCU = field(init=False)

    def __post_init__(self) -> None:
        self.influxdb = INFLUX_DB
        self.ccu = CCU
