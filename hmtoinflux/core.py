import time
import requests

from hm import StateList, DeviceList, RoomList
from . import config
from xml.etree.ElementTree import ParseError

from hmtoinflux.influxDataBuilder import InfluxDataBuilder

stateList = {}
deviceList = {}
roomList = {}

apiurl = 'http://'+config.source.ccu.address+'/addons/xmlapi/'

def updateDevices():
    xml = requests.get(apiurl + 'devicelist.cgi')
    deviceList.rebuild(xml.text)

def updateRoom():
    xml = requests.get(apiurl + 'roomlist.cgi')
    roomList.rebuild(xml.text)

def updateState():
    xml = requests.get(apiurl + 'statelist.cgi')
    stateList.rebuild(xml.text)

def Core():
    global deviceList, stateList, roomList
    print('HMTOINFLUX: started with source: ' + config.base.source)
    if config.base.source == 'ccu':
        count = 0

        xml = requests.get(apiurl + 'devicelist.cgi')
        deviceList = DeviceList(xml.text)
        xml = requests.get(apiurl + 'statelist.cgi')
        stateList = StateList(xml.text)
        xml = requests.get(apiurl + 'roomlist.cgi')
        roomList = RoomList(xml.text)
        while 1:
            try:
                if count > 6:
                    updateDevices()
                    updateRoom()
                updateState()
                builder = InfluxDataBuilder(stateList, deviceList, roomList)
                builder.write_state_data()
            except (ParseError, ConnectionError):
                pass
            time.sleep(10)
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

        builder = InfluxDataBuilder(stateList, deviceList, roomList)
        while 1:
            builder.write_state_data()
            time.sleep(1)