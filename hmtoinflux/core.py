import time
import requests

from hm import StateList, DeviceList, RoomList
from . import config

from hmtoinflux.influxDataBuilder import InfluxDataBuilder

stateList = {}
deviceList = {}
roomList = {}


def Core():
    print('HMTOINFLUX: started with source: ' + config.base.source)
    if config.base.source == 'ccu':
        xml = requests.get('http://ccu3-webui/config/xmlapi/devicelist.cgi')
    else:
        xml = open('testdata/statelist_old.xml', "r", encoding="ISO-8859-1")
        stateList = StateList(xml.read())
        xml.close()

        xml = open('testdata/devicelist.xml', "r", encoding="ISO-8859-1")
        deviceList = DeviceList(xml.read())
        xml.close()

        xml = open('testdata/roomlist.xml', "r", encoding="ISO-8859-1")
        roomList = RoomList(xml.read())
        xml.close()

        builder = InfluxDataBuilder(stateList, deviceList, roomList)
        while 1:
            builder.write_state_data()
            time.sleep(1)