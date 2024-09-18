import unittest
import csv
import os
from io import StringIO
from utils import read_csv, write_csv, apply_changes


class TestCSVReader(unittest.TestCase):

    def setUp(self):
        self.input_data = [
            ['door', '3', '7', '0'],
            ['sandwich', '12', '5', '1'],
            ['brush', '22', '34', '5'],
            ['poster', 'red', '8', 'stick']
        ]
        self.changes = ['0,0,guitar', '3,1,mug', '1,2,17', '3,3,0']
        self.expected_output_data = [
            ['guitar', '3', '7', '0'],
            ['sandwich', '12', '5', 'mug'],
            ['brush', '17', '34', '5'],
            ['poster', 'red', '8', '0']
        ]

    def test_read_csv(self):
        input_csv = StringIO("""door,3,7,0
sandwich,12,5,1
brush,22,34,5
poster,red,8,stick
""")
        with open('test_in.csv', 'w', newline='', encoding='utf-8') as file:
            file.write(input_csv.getvalue())

        result = read_csv('test_in.csv')
        self.assertEqual(result, self.input_data)
        os.remove('test_in.csv')

    def test_write_csv(self):
        write_csv('test_out.csv', self.expected_output_data)

        with open('test_out.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            result = [row for row in reader]
            self.assertEqual(result, self.expected_output_data)

        os.remove('test_out.csv')

    def test_apply_changes(self):
        modified_data = apply_changes(self.input_data, self.changes)
        self.assertEqual(modified_data, self.expected_output_data)

    def test_invalid_change_format(self):
        invalid_changes = ['a,b,value']
        with self.assertRaises(ValueError):
            apply_changes(self.input_data, invalid_changes)

    def test_out_of_bounds_index(self):
        out_of_bounds_changes = ['10,10,value']
        with self.assertRaises(IndexError):
            apply_changes(self.input_data, out_of_bounds_changes)

if __name__ == '__main__':
    unittest.main()