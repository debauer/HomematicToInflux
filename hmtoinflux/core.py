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

print("homematic api url: " + apiurl)

def updateDevices():
    xml = requests.get(apiurl + 'devicelist.cgi')
    deviceList.rebuild(xml.text)

def updateRoom():
    xml = requests.get(apiurl + 'roomlist.cgi')
    roomList.rebuild(xml.text)

def updateState():
    print("updateState: started")
    xml = requests.get(apiurl + 'statelist.cgi')
    stateList.rebuild(xml.text)
    print("updateState: ready")

def Core():
    global deviceList, stateList, roomList
    print('HMTOINFLUX: started with source: ' + config.base.source)
    if config.base.source == 'ccu':
        print('HMTOINFLUX: okey get the data from the CCU')
        count = 0
        xml = requests.get(apiurl + 'devicelist.cgi')
        deviceList = DeviceList(xml.text)
        xml = requests.get(apiurl + 'statelist.cgi')
        stateList = StateList(xml.text)
        xml = requests.get(apiurl + 'roomlist.cgi')
        roomList = RoomList(xml.text)
        while 1:
            print("update runs...")
            try:
                if count > 6:
                    updateDevices()
                    updateRoom()
                updateState()
                builder = InfluxDataBuilder(stateList, deviceList, roomList)
                builder.write_state_data()
            except (ParseError, ConnectionError):
                print(ParseError)
                print(ConnectionError)
                pass
            print("update done")
            time.sleep(10)
    else:
        print('HMTOINFLUX: we use demo data ')
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