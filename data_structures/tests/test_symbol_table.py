import unittest
from data_structures.entry import Entry
from data_structures.symbol_table import SymbolTable

class TestSymbolTable(unittest.TestCase):
    def setUp(self):
        self.table = SymbolTable('test')

    def test_insert_entry(self):
        """Test that the entry is inserted correctly
        """

        self.table.insert_entry('test_token')
        self.assertEqual(len(self.table.entries), 1, 'The length of the entry list is not 1 after an insertion.')
        self.assertEqual(self.table.entries[0][1].content, 'test_token', 'The content of the entry inserted is not correct.')
    
    def test_exists(self):
        """Test that the method returns true if the entry exist, and false if it does not exist
        """

        self.table.insert_entry('test_token')
        self.assertTrue(self.table.exists('test_token'), 'An existing token returns false.')
        self.assertFalse(self.table.exists('not_exist'), 'A non-existing token returns true.')

    def test_get_entry_with_token(self):
        """Test that the correct entry with the token is returned
        """

        self.table.insert_entry('test_token')
        expected_entry = self.table.entries[0]
        self.assertTupleEqual(self.table.get_entry_with_token('test_token'), expected_entry, 'An existing entry did not get returned.')
        self.assertIsNone(self.table.get_entry_with_token('not_exist'), 'A non-existing entry did not return None.')
    
    def test_get_entries(self):
        """Test that the list of entries is returned correctly
        """

        expected_entries = [(0, 'test_token')]
        self.table.insert_entry('test_token')
        output = self.table.get_entries()
        self.assertListEqual(output, expected_entries)