import os
import requests
import sys
from python_json_config import ConfigBuilder

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from hm import StateList, DeviceList, RoomList

builder = ConfigBuilder()

config = builder.parse_config('config.json')

stateList = {}
deviceList = {}
roomList = {}

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


    def printStateList():
        stateList.print_all_states()


    def printRoomList():
        roomList.print_all_rooms()


    def printDatapoints():
        d = stateList.get_state_by_name('EG_Wohnz_Temp_Feuchte')
        if d:
            datapoints = d.get_datapoints()
            for datapoint in datapoints:
                print(datapoint)


    def printDeviceList():
        deviceList.print_all_devices()


    def printDeviceList():
        deviceList.print_all_devices()

    printRoomList()
    printDeviceList()
    printStateList()
    #printDatapoints()
