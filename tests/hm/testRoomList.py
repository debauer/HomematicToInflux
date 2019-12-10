import unittest
from hm import Roomlist


class HmRoomListTest(unittest.TestCase):
    def testImport(self):
        xml = open("testdata/roomlist.xml", "r", encoding="ISO-8859-1")
        xml_string = xml.read()
        rl = Roomlist(xml_string)
        self.assertEqual(rl.get_xml(), xml_string)
        self.assertEqual(rl.get_room_count(), 19)
        xml.close()


if __name__ == '__main__':
    unittest.main()
