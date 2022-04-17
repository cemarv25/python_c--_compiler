import unittest
from data_structures.entry import Entry
from data_structures.symbol_table import SymbolTable

class TestSymbolTable(unittest.TestCase):
    def test_insert_entry(self):
        table = SymbolTable('test')
        table.insert_entry('test_token')
        self.assertEqual(len(table.entries), 1, 'The length of the entry list is not 1 after an insertion.')
        self.assertEqual(table.entries[0][1].content, 'test_token', 'The content of the entry inserted is not correct.')
    
    def test_exists(self):
        table = SymbolTable('test')
        table.insert_entry('test_token')
        self.assertTrue(table.exists('test_token'), 'An existing token returns false.')
        self.assertFalse(table.exists('not_exist'), 'A non-existing token returns true.')

    def test_get_entry_with_token(self):
        table = SymbolTable('test')
        table.insert_entry('test_token')
        expected_entry = table.entries[0]
        self.assertTupleEqual(table.get_entry_with_token('test_token'), expected_entry, 'An existing entry did not get returned.')
        self.assertIsNone(table.get_entry_with_token('not_exist'), 'A non-existing entry did not return None.')