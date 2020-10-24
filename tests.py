import unittest

import csv2sql

class SampleTest(unittest.TestCase):
    def test_open_file(self):
        f = csv2sql.open_file("test.csv")
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
