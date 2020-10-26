import unittest

import csv2sql

class SampleTest(unittest.TestCase):

    def test_open_file(self):
        f = csv2sql.open_file('test.csv')
        self.assertTrue(f)
        f.close()

    def test_parse_columns(self):
        columns_line = ',COLUMN1,COLUMN2,,COLUMN3,'
        expected = ['','COLUMN1', 'COLUMN2', '', 'COLUMN3', '']
        result = csv2sql.parse_columns(columns_line)
        self.assertEqual(result, expected)

    def test_input(self):
        f = open('test.csv', 'w')
        f.write('column1,columns2,column3,column4\n')
        f.write(',value2,value3,value4\n')
        f.close()
        f = open('test.csv', 'r')
        titles = csv2sql.get_titles(f)
        expected_titles= ['column1','columns2','column3','column4']
        self.assertEqual(expected_titles, titles)
        f.close()

if __name__ == '__main__':
    unittest.main()
