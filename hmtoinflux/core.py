from datetime import datetime
import time
from random import random

import requests
from python_json_config import ConfigBuilder

from hm import StateList, DeviceList, RoomList

builder = ConfigBuilder()

config = builder.parse_config('config.json')

stateList = {}
deviceList = {}
roomList = {}


def Core():
    print('HMTOINFLUX: started with source: ' + config.base.source)
    if config.base.source == 'ccu':
        xml = requests.get('http://ccu3-webui/config/xmlapi/devicelist.cgi')
    else:
        xml = open('testdata/statelist.xml', "r", encoding="ISO-8859-1")
        stateList = StateList(xml.read())
        xml.close()

        xml = open('testdata/devicelist.xml', "r", encoding="ISO-8859-1")
        deviceList = DeviceList(xml.read())
        xml.close()

        xml = open('testdata/roomlist.xml', "r", encoding="ISO-8859-1")
        roomList = RoomList(xml.read())
        xml.close()

        from influxdb import InfluxDBClient
        client = InfluxDBClient('localhost', 8086, 'root', 'root', 'homematicToInflux')

        while 1:
            json_body = [
                {
                    "measurement": "cpu_load_short",
                    "tags": {
                        "host": "server01",
                        "region": "us-west"
                    },
                    "fields": {
                        "value": random()
                    }
                }
            ]
            print(json_body)

            client.write_points(json_body)
            time.sleep(1);
