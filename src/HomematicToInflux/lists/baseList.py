from abc import abstractmethod

import requests


class BaseList:
    def __init__(self, address: str, mode: str):
        self.xml = ""
        self.apiurl = 'http://' + address + '/addons/xmlapi/'
        self.encoding = "ISO-8859-1"
        self.endpoint = ""
        self.update_mode = mode

    def update(self) -> None:
        if self.update_mode == "ccu":
            self.xml = requests.get(f"{self.apiurl}{self.__class__.__name__.lower()}.cgi")
            self.rebuild(self.xml.text)
        else:
            xml = open(f'testdata/{self.__class__.__name__.lower()}.xml', "r", encoding="ISO-8859-1")
            self.rebuild(xml.read())
            xml.close()

    @abstractmethod
    def rebuild(self, xml: str):
        pass

    def get_xml(self):
        return self.xml

    def set_encoding(self, encoding):
        self.encoding = encoding
