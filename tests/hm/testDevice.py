import unittest
from hm import Device


class HmDeviceTest(unittest.TestCase):
    def testDevice(self):
        device = Device("device 1337", 12, 'ASD678ASD', 'device type yolo')
        self.assertEqual(device.get_name(), 'device 1337')
        self.assertEqual(device.get_ise_id(), 12)
        self.assertEqual(device.get_address(), 'ASD678ASD')
        self.assertEqual(device.get_device_type(), 'device type yolo')


if __name__ == '__main__':
    unittest.main()
