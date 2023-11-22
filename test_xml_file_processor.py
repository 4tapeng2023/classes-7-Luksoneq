import unittest
import os
from unittest.mock import patch, MagicMock
import xml.etree.ElementTree as ET
from xml_file_processor import FileProcessor

class TestFileProcessor(unittest.TestCase):

    def setUp(self):
        self.filename = 'test_temp.xml'
        with open(self.filename, 'w') as file:
            file.write('<root></root>')
        self.processor = FileProcessor()

    def test_add_and_display_record(self):
        person_data = {'name': 'John', 'age': '30', 'address': {'street': '123 Test St', 'city': 'Testville', 'state': 'TS', 'zip': '12345'}}
        self.processor.add_record(self.filename, person_data)
        root = self.processor.read_file(self.filename)
        self.assertIsNotNone(root.find("./person[name='John']"))
        
        
        self.processor.display_records(self.filename)  

    def test_update_record(self):
        updated_person_data = {'name': 'John', 'age': '31', 'address': {'street': '456 Test St', 'city': 'Newville', 'state': 'NS', 'zip': '54321'}}
        self.processor.update_record(self.filename, 'John', updated_person_data)
        root = self.processor.read_file(self.filename)
        updated_person = root.find("./person[name='John']")
        self.assertIsNotNone(updated_person)
        self.assertEqual(updated_person.find('age').text, '31')

    def test_delete_record(self):
        self.processor.delete_record(self.filename, 'John')
        root = self.processor.read_file(self.filename)
        self.assertIsNone(root.find("./person[name='John']"))

    def tearDown(self):
        os.remove(self.filename)

    @patch('xml.etree.ElementTree.parse')
    def test_read_file_with_mock(self, mock_parse):
        mock_tree = ET.ElementTree(ET.fromstring('<root><person><name>John</name></person></root>'))
        mock_parse.return_value = mock_tree

        root = self.processor.read_file('dummy.xml')
        self.assertIsNotNone(root.find("./person[name='John']"))

    @patch('xml.etree.ElementTree.ElementTree.write')
    def test_add_record_with_mock(self, mock_write):
        mock_write.return_value = None

        person_data = {'name': 'Jane', 'age': '29', 'address': {'street': '789 Test St', 'city': 'Test City', 'state': 'TC', 'zip': '98765'}}
        self.processor.add_record(self.filename, person_data)
        mock_write.assert_called_once()

    @patch('xml.etree.ElementTree.ElementTree.write')
    def test_delete_record_with_mock(self, mock_write):
        mock_write.return_value = None

        self.processor.delete_record(self.filename, 'Jane')
        mock_write.assert_called_once()

    @patch('xml.etree.ElementTree.ElementTree.write')
    def test_update_record_with_mock(self, mock_write):
        mock_write.return_value = None

        updated_person_data = {'name': 'Jane', 'age': '30', 'address': {'street': '101 Test St', 'city': 'New Test City', 'state': 'NT', 'zip': '10101'}}
        self.processor.update_record(self.filename, 'Jane', updated_person_data)
        self.assertEqual(mock_write.call_count, 2)


if __name__ == '__main__':
    unittest.main()