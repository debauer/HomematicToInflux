from dataclasses import dataclass, field

from hmtoinflux.config import INFLUX_DB, CCU
from hmtoinflux.config_wrapper.types import HomematicCCU, InfluxDB


@dataclass
class ConfigWrapper:
    influxdb: InfluxDB = field(init=False)
    ccu: HomematicCCU = field(init=False)

    def __post_init__(self):
        self.influxdb = INFLUX_DB
        self.ccu = CCU
