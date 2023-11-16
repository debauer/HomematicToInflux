from __future__ import annotations

from hmtoinflux.config_wrapper.types import HomematicCCU
from hmtoinflux.config_wrapper.types import InfluxDB


CCU = HomematicCCU(address="192.168.1.105")

INFLUX_DB = InfluxDB(
    address="herbert",
    user="homematic",
    auth=True,
    port=8086,
    password="asdf",  # noqa: S106
    database_name="homematic",
    bulk_size=5,
)
