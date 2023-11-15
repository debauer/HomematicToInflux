import time
from argparse import ArgumentParser, Namespace

from hmtoinflux.config_wrapper.wrapper import ConfigWrapper
from hmtoinflux.data_builder.builder import InfluxDataBuilder
from hmtoinflux.lists import DeviceList, RoomList, StateList


def parse_args() -> Namespace:
    parser = ArgumentParser(description="scan image")
    parser.add_argument("-s", "--source", type=str, choices=["ccu", "file"], default="ccu")
    parser.add_argument("-d", "--dryrun", action="store_const", const="dryrun", help="don't commit to influxdb")
    parser.add_argument("-v", "--verbose", action="store_const", const="verbose", help="verbose")
    return parser.parse_args()


def core() -> None:
    args = parse_args()
    source = args.source
    verbose = args.verbose
    dryrun = args.dryrun
    config = ConfigWrapper()
    devices = DeviceList(config.ccu.address, mode=source)
    rooms = RoomList(config.ccu.address, mode=source)
    states = StateList(config.ccu.address, mode=source)
    builder = InfluxDataBuilder(states, devices, rooms)
    print("[HMTOINFLUX] started with source: " + source)
    print(f"[args] {args}")
    count = 0
    while 1:
        if count > 6:
            if verbose:
                print(f"[update] devices and rooms")
            devices.update()
            rooms.update()
        if verbose:
            print(f"[update] states")
        states.update()
        if not dryrun:
            if verbose:
                print(f"[influx] run datapoint builder")
            builder.update()
        time.sleep(10)


if __name__ == "__main__":
    core()
