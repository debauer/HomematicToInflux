from __future__ import annotations

from abc import abstractmethod
from pathlib import Path

import requests


class BaseList:
    def __init__(self, address: str, mode: str) -> None:
        self.xml = ""
        self.apiurl = "http://" + address + "/addons/xmlapi/"
        self.encoding = "ISO-8859-1"
        self.endpoint = ""
        self.update_mode = mode

    def update(self) -> None:
        if self.update_mode == "ccu":
            self.xml = requests.get(
                f"{self.apiurl}{self.__class__.__name__.lower()}.cgi",
                timeout=5,
            ).text
            self.rebuild(self.xml)
        else:
            with Path(f"testdata/{self.__class__.__name__.lower()}.xml").open() as xml:
                self.rebuild(xml.read())

    @abstractmethod
    def rebuild(self, xml: str) -> None:
        ...

    def get_xml(self) -> str:
        return self.xml

    def set_encoding(self, encoding: str) -> None:
        self.encoding = encoding
