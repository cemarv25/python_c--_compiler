from data_structures.symbol_table import SymbolTable
import unittest
import main

class TestScanner(unittest.TestCase):
    def setUp(self):
        self.id_sym_table = SymbolTable('ids')
        self.num_sym_table = SymbolTable('nums')

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
            (21, 4), 9, 19, 19, 5, (20, 11), 14, 5, 15, 18, 3, (20, 5), 9, (20, 5), 25, (21, 5), 9, 6, 14, (20, 5), 21, (21, 6),
            15, 18, 7, (20, 0), 16, (20, 5), 17, 9, (20, 5), 25, (20, 5), 11, (21, 7), 9, 19, (20, 7), 14, (20, 0), 10, (21, 8),
            10, (21, 9), 15, 9, (20, 5), 25, (21, 10), 9, 6, 14, (20, 5), 21, (21, 11), 15, 18, 8, (20, 0), 16, (20, 5), 17, 9,
            (20, 5), 25, (20, 5), 11, (21, 12), 9, 19, 19
        ]
        f = open('scanner/test1.txt', 'r')
        token_seq = main.recognize_tokens(self.id_sym_table, self.num_sym_table, f)
        f.close()
        self.assertListEqual(token_seq, expected_token_seq_1, "The token sequence does not equal the expected.")

    def test_outputs_bad_pseudotoken_msg(self):
        """Test that the scanner detects a bad pseudotoken and outputs the correct message.
        """

        expected_output = 'BadPseudoToken: Identifier or reserved word badly constructed.\n\tAt scanner/tests/text_files/test_bad_pseudotoken.txt:1'
        f = open('scanner/tests/text_files/test_bad_pseudotoken.txt', 'r')
        output = main.recognize_tokens(self.id_sym_table, self.num_sym_table, f)
        f.close()
        self.assertEqual(output, expected_output)

    def test_outputs_bad_number_msg(self):
        """Test that the scanner detects a bad number and outputs the correct message.
        """

        expected_output = 'BadNumber: Number literal badly constructed.\n\tAt scanner/tests/text_files/test_bad_number.txt:1'
        f = open('scanner/tests/text_files/test_bad_number.txt', 'r')
        output = main.recognize_tokens(self.id_sym_table, self.num_sym_table, f)
        f.close()
        self.assertEqual(output, expected_output)

    def test_outputs_bad_exclamation_msg(self):
        """Test that the scanner detects a bad number and outputs the correct message.
        """

        expected_output = 'UnexpectedChar: Unexpected "!" encountered.\n\tAt scanner/tests/text_files/test_bad_!.txt:1'
        f = open('scanner/tests/text_files/test_bad_!.txt', 'r')
        output = main.recognize_tokens(self.id_sym_table, self.num_sym_table, f)
        f.close()
        self.assertEqual(output, expected_output)

    def test_outputs_bad_compound_sym_msg(self):
        """Test that the scanner detects a bad compound symbol and outputs the correct message.
        """

        expected_output = 'BadCompoundSymbol: Compound symbol badly constructed.\n\tAt scanner/tests/text_files/test_bad_compound_sym.txt:1'
        f = open('scanner/tests/text_files/test_bad_compound_sym.txt', 'r')
        output = main.recognize_tokens(self.id_sym_table, self.num_sym_table, f)
        f.close()
        self.assertEqual(output, expected_output)

    def test_outputs_rare_sym_msg(self):
        """Test that the scanner detects a rare symbol and outputs the correct message.
        """

        expected_output = 'UnexpectedChar: A character that does not belong to the language\'s alphabet was encountered.\n\tAt scanner/tests/text_files/test_rare_sym.txt:1'
        f = open('scanner/tests/text_files/test_rare_sym.txt', 'r')
        output = main.recognize_tokens(self.id_sym_table, self.num_sym_table, f)
        f.close()
        self.assertEqual(output, expected_output)

    def test_outputs_non_closing_comment_msg(self):
        """Test that the scanner detects a non-closing comment and outputs the correct message.
        """

        expected_output = 'NonClosingComment: The EOF was reached with a non-closing comment.\n\tAt scanner/tests/text_files/test_non_closing_comment.txt:2'
        f = open('scanner/tests/text_files/test_non_closing_comment.txt', 'r')
        output = main.recognize_tokens(self.id_sym_table, self.num_sym_table, f)
        f.close()
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()