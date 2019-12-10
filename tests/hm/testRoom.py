import unittest
from hm import Room


class HmRoomTest(unittest.TestCase):
    def testRoom(self):
        r = Room("testraum", 123, [1, 2, 3, 4, 5])
        self.assertEqual(r.get_name(), "testraum")
        self.assertEqual(r.get_channels(), [1, 2, 3, 4, 5])
        self.assertEqual(r.get_ise_id(), 123)
        self.assertTrue(r.is_id_in_channels(1))
        self.assertFalse(r.is_id_in_channels(0))


if __name__ == '__main__':
    unittest.main()
