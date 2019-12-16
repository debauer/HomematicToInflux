import unittest
from hm import DeviceList, Device


class HmDeviceListTest(unittest.TestCase):
    def testDeviceList(self):
        xml = open("testdata/devicelist.xml", "r", encoding="ISO-8859-1")
        xml_string = xml.read()
        rl = DeviceList(xml_string)
        self.assertEqual(rl.get_xml(), xml_string)
        self.assertIsInstance(rl.get_device_by_name('EG_Wohnz_Temp_Feuchte'), Device)
        self.assertEqual(rl.get_device_by_name('not_valid'), None)
        self.assertEqual(rl.get_device_count(), 25)
        xml.close()

if __name__ == '__main__':
    unittest.main()
