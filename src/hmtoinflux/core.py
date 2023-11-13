import time
from argparse import ArgumentParser, Namespace

from hmtoinflux.data_builder.builder import InfluxDataBuilder
from hmtoinflux.lists import DeviceList, RoomList, StateList


#


def parse_args() -> Namespace:
    parser = ArgumentParser(description="scan image")
    parser.add_argument("--source", type=str, choices=["ccu", "file"], default="ccu")
    parser.add_argument("--address", type=str, default="192.168.1.105")
    return parser.parse_args()


def core() -> None:
    args = parse_args()
    source = args.source
    ccu_address = args.address
    devices = DeviceList(ccu_address, mode=source)
    rooms = RoomList(ccu_address, mode=source)
    states = StateList(ccu_address, mode=source)
    builder = InfluxDataBuilder(states, devices, rooms)
    print("[HMTOINFLUX] started with source: " + source)
    count = 0
    while 1:
        if count > 6:
            devices.update()
            rooms.update()
        states.update()
        builder.update()
        time.sleep(10)


if __name__ == "__main__":
    core()
