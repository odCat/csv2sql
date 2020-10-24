import unittest

import csv2sql

class SampleTest(unittest.TestCase):
    def test_open_file(self):
        f = csv2sql.open_file("test.csv")
        self.assertTrue(f)
        f.close()
    def test_parse_columns(self):
        columns_line = "COLUMN1,COLUMN2,COLUMN3"
        expected = ["COLUMN1", "COLUMN2", "COLUMN3"]
        result = csv2sql.parse_columns(columns_line)
        self.assertTrue(result == expected)
        columns_line = ",COLUMN1,COLUMN2,,COLUMN3,"
        expected = ["","COLUMN1", "COLUMN2", "", "COLUMN3", ""]
        result = csv2sql.parse_columns(columns_line)
        self.assertTrue(result == expected)

if __name__ == '__main__':
    unittest.main()
