

class BaseList:
    def __init__(self, xml):
        self.xml = xml
        self.encoding = "ISO-8859-1"

    def get_xml(self):
        return self.xml

    def set_encoding(self,encoding):
        self.encoding = encoding