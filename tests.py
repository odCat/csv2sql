import os
import unittest

import csv2sql

class Csv2sqlTests(unittest.TestCase):
    test_file = 'test.csv'

    def setUp(self):
        f = open(self.test_file, 'w')
        f.write('column1,column2,column3,column4\n')
        f.write(',value2,value3,value4\n')
        f.write(',value21,value3,value4')
        f.close()

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        else:
            print('The file does not exist')

    def test_open_file(self):
        f = csv2sql.open_file(self.test_file)
        self.assertTrue(f)
        f.close()

    def test_add_escape(self):
        tested = "test'test'test"
        expected = "test''test''test"
        self.assertEqual(expected, csv2sql.add_escape(tested))

    def test_parse_columns(self):
        columns_line = ',COLUMN1,COLUMN2,,COLUMN3,'
        expected = ['','COLUMN1', 'COLUMN2', '', 'COLUMN3', '']
        result = csv2sql.parse_columns(columns_line)
        self.assertEqual(result, expected)

    def test_get_titles(self):
        f = open(self.test_file, 'r', encoding="utf-8")
        titles = csv2sql.get_titles(f)
        expected_titles= ['column1','column2','column3','column4']
        self.assertEqual(expected_titles, titles)
        f.close()

    def test_get_rows(self):
        f = open(self.test_file, 'r', encoding="utf-8")
        f.readline()
        rows = csv2sql.get_rows(f)
        expected_rows = [['','value2','value3','value4'],
                         ['','value21','value3','value4']]
        self.assertEqual(expected_rows, rows)
        f.close()

    def test_generate_sql(self):
        f = open(self.test_file, 'r', encoding="utf-8")
        titles = csv2sql.get_titles(f)
        rows = csv2sql.get_rows(f)
        expected_sql = (
                'select\n'
                '\tcolumn1 as column1,\n'
                '\tcolumn2 as column2,\n'
                '\tcolumn3 as column3,\n'
                '\tcolumn4 as column4\n'
                'from values\n'
                "\t(null,'value2','value3','value4'),\n"
                "\t(null,'value21','value3','value4')\n"
                ';')
        self.assertEqual(expected_sql,
                         csv2sql.generate_sql(titles, rows))
        f.close()

if __name__ == '__main__':
    unittest.main()
