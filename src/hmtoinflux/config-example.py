from hmtoinflux.config_wrapper.types import InfluxDB, HomematicCCU


CCU = HomematicCCU(
    address="192.168.1.105"
)


INFLUX_DB = InfluxDB(
    address="herbert",
    user="homematic",
    auth=True,
    port=8086,
    password="asdf",
    database_name="homematic",
    bulk_size=5
)