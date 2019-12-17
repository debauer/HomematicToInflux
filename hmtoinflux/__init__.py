import sys
import os

from python_json_config import ConfigBuilder
from influxdb import InfluxDBClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
InfluxClient = InfluxDBClient('localhost', 8086, 'root', 'root', 'homematicToInflux')
builder = ConfigBuilder()
config = builder.parse_config('config.json')

from .core import Core
