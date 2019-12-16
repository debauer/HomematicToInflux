import unittest
from hm import State


class HmStateTest(unittest.TestCase):
    def testState(self):
        state = State("state 1337", 12, [1, 2])
        self.assertEqual(state.get_name(), 'state 1337')
        self.assertEqual(state.get_ise_id(), 12)
        self.assertEqual(len(state.get_channels()), 2)


if __name__ == '__main__':
    unittest.main()
