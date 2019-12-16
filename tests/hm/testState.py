import unittest
from hm import State

dp1 = {'ise_id': '1463', 'name': 'OPERATING_VOLTAGE', 'operations': '5', 'timestamp': '1575232894',
       'type': 'OPERATING_VOLTAGE', 'value': '3.000000', 'valuetype': '4', 'valueunit': ''}
dp2 = {'ise_id': '1487', 'name': 'HUMIDITY', 'operations': '5', 'timestamp': '1575232894', 'type': 'HUMIDITY',
       'value': '40', 'valuetype': '16', 'valueunit': ''}


class HmStateTest(unittest.TestCase):

    def setUp(self):
        self.state = State("state 1337", 12, [dp1, dp2])

    def testGetName(self):
        self.assertEqual(self.state.get_name(), 'state 1337')

    def testGetIseId(self):
        self.assertEqual(self.state.get_ise_id(), 12)

    def testGetDatapoints(self):
        self.assertEqual(len(self.state.get_datapoints()), 2)

    def testGetDatapointByName(self):
        self.assertEqual(self.state.get_datapoint_by_name('OPERATING_VOLTAGE'), dp1)
        self.assertEqual(self.state.get_datapoint_by_name('HUMIDITY'), dp2)

    def tearDown(self):
        self.state = None


if __name__ == '__main__':
    unittest.main()
