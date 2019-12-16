import unittest
from hm import StateList, State


class HmStateListTest(unittest.TestCase):
    def testStateList(self):
        xml = open("testdata/devicelist.xml", "r", encoding="ISO-8859-1")
        xml_string = xml.read()
        rl = StateList(xml_string)
        self.assertEqual(rl.get_xml(), xml_string)
        self.assertIsInstance(rl.get_state_by_name('EG_Wohnz_Temp_Feuchte'), State)
        xml.close()

if __name__ == '__main__':
    unittest.main()
