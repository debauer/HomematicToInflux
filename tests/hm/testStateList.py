import unittest
from hm import StateList, State


class HmStateListTest(unittest.TestCase):
    def setUp(self):
        self.xml = open("testdata/devicelist.xml", "r", encoding="ISO-8859-1")
        self.xml_string = self.xml.read()
        self.stateList = StateList(self.xml_string)

    def testGetXml(self):
        self.assertEqual(self.stateList.get_xml(), self.xml_string)

    def testGetStateByName(self):
        self.assertIsInstance(self.stateList.get_state_by_name('EG_Wohnz_Temp_Feuchte'), State)

    def tearDown(self):
        self.stateList = None
        self.xml.close()


if __name__ == '__main__':
    unittest.main()
