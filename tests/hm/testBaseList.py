import unittest
from hm import BaseList


class HmBaseTest(unittest.TestCase):
    def testBase(self):
        xml = "<hallo>asd</hallo>"
        r = BaseList(xml)
        self.assertEqual(r.get_xml(), xml)


if __name__ == '__main__':
    unittest.main()
