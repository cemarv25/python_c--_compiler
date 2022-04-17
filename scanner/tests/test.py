from data_structures.symbol_table import SymbolTable
import unittest
import main

class TestScanner(unittest.TestCase):
    def test_recognize_tokens(self):
        """Test that the scanner outputs the correct token sequence.
        """

        expected_token_seq_1 = [
            3, (20, 0), 16, (21, 0), 17, 9, 3, (20, 1), 14, 3, (20, 2), 16, 17, 10, 3, (20, 3), 10, 3, (20, 4), 15, 18, 3,
            (20, 5), 9, 3, (20, 0), 9, 3, (20, 6), 9, (20, 6), 25, (20, 3), 9, (20, 0), 25, (20, 2), 16, (20, 3), 17, 9, (20, 5),
            25, (20, 3), 11, (21, 1), 9, 6, 14, (20, 5), 21, (20, 4), 15, 18, 2, 14, (20, 2), 16, (20, 5), 17, 21, (20, 0), 15,
            18, (20, 0), 25, (20, 2), 16, (20, 5), 17, 9, (20, 6), 25, (20, 5), 9, 19, (20, 5), 25, (20, 5), 11, (21, 2), 9, 19,
            4, (20, 6), 9, 19, 5, (20, 7), 14, 3, (20, 2), 16, 17, 10, 3, (20, 3), 10, 3, (20, 4), 15, 18, 3, (20, 5), 9, 3,
            (20, 6), 9, (20, 5), 25, (20, 3), 9, 6, 14, (20, 5), 21, (20, 4), 12, (21, 3), 15, 18, 3, (20, 8), 9, (20, 6), 25,
            (20, 9), 14, (20, 2), 10, (20, 10), 10, (20, 4), 15, 9, (20, 8), 25, (20, 2), 16, (20, 6), 17, 9, (20, 2), 16,
            (20, 6), 17, 25, (20, 2), 16, (20, 5), 17, 9, (20, 2), 16, (20, 5), 17, 25, (20, 8), 9, (20, 5), 25, (20, 5), 11,
            (21, 4), 9, 19, 19
        ]
        id_sym_table = SymbolTable("ids")
        num_sym_table = SymbolTable("nums")
        f = open('scanner/test1.txt', 'r')
        self.assertListEqual(main.recognize_tokens(id_sym_table, num_sym_table, f), expected_token_seq_1)
        f.close()

if __name__ == '__main__':
    unittest.main()