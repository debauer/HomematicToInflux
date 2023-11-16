from __future__ import annotations

import time

from argparse import ArgumentParser
from argparse import Namespace
from logging import getLogger

from hmtoinflux.config_wrapper.wrapper import ConfigWrapper
from hmtoinflux.data_builder.builder import InfluxDataBuilder
from hmtoinflux.lists import DeviceList
from hmtoinflux.lists import RoomList
from hmtoinflux.lists import StateList


_log = getLogger()

STATE_UPDATE_EVERY_SEC = 10
DEVICE_AND_ROOM_UPDATE_EVERY_SEC = 60


def parse_args() -> Namespace:
    parser = ArgumentParser(description="scan image")
    parser.add_argument(
        "-s",
        "--source",
        type=str,
        choices=["ccu", "file"],
        default="ccu",
    )
    parser.add_argument(
        "-d",
        "--dryrun",
        action="store_const",
        const="dryrun",
        help="don't commit to influxdb",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_const",
        const="verbose",
        help="verbose",
    )
    return parser.parse_args()


def core() -> None:
    args = parse_args()
    source = args.source
    dryrun = args.dryrun
    config = ConfigWrapper()
    devices = DeviceList(config.ccu.address, mode=source)
    rooms = RoomList(config.ccu.address, mode=source)
    states = StateList(config.ccu.address, mode=source)
    builder = InfluxDataBuilder(states, devices, rooms)
    _log.info("[HMTOINFLUX] started with source: " + source)
    _log.info(f"[args] {args}")
    count = 0
    while 1:
        if count > DEVICE_AND_ROOM_UPDATE_EVERY_SEC / STATE_UPDATE_EVERY_SEC:
            _log.debug("[update] devices and rooms")
            devices.update()
            rooms.update()
        _log.debug("[update] states")
        states.update()
        if not dryrun:
            _log.debug("[influx] run datapoint builder")
            builder.update()
        time.sleep(STATE_UPDATE_EVERY_SEC)


if __name__ == "__main__":
    core()
