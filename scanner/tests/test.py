import unittest
import main

class TestScanner(unittest.TestCase):
    def test_recognize_tokens(self):
        """Test that the scanner outputs the correct token sequence.
        """

        expected_token_seq_1 = [
            33, (10, 0), 19, (11, 0), 20, 12, 33, (10, 1), 17, 33, (10, 2), 19, 20, 13, 33, (10, 3), 13, 33, (10, 4), 18,
            21, 33, (10, 5), 12, 33, (10, 0), 12, 33, (10, 6), 12, (10, 6), 28, (10, 3), 12, (10, 0), 28, (10, 2), 19, (10, 3),
            20, 12, (10, 5), 28, (10, 3), 14, (11, 1), 12, 36, 17, (10, 5), 24, (10, 4), 18, 21, 32, 17, (10, 2), 19, (10, 5),
            20, 24, (10, 0), 18, 21, (10, 0), 28, (10, 2), 19, (10, 5), 20, 12, (10, 6), 28, (10, 5), 12, 22, (10, 5), 28,
            (10, 5), 14, (11, 1), 12, 22, 34, (10, 6), 12, 22, 35, (10, 7), 17, 33, (10, 2), 19, 20, 13, 33, (10, 3), 13,
            33, (10, 4), 18, 21, 33, (10, 5), 12, 33, (10, 6), 12, (10, 5), 28, (10, 3), 12, 36, 17, (10, 5), 24, (10, 4),
            15, (11, 1), 18, 21, 33, (10, 8), 12, (10, 6), 28, (10, 9), 17, (10, 2), 13, (10, 10), 13, (10, 4), 18, 12,
            (10, 8), 28, (10, 2), 19, (10, 6), 20, 12, (10, 2), 19, (10, 6), 20, 28, (10, 2), 19, (10, 5), 20, 12, (10, 2),
            19, (10, 5), 20, 28, (10, 8), 12, (10, 5), 28, (10, 5), 14, (11, 1), 12, 22, 22, 35, (10, 11), 17, 35, 18, 21,
            33, (10, 5), 12, (10, 5), 28, (11, 2), 12, 36, 17, (10, 5), 24, (11, 0), 18, 21, 37, (10, 0), 19, (10, 5), 20,
            12, (10, 5), 28, (10, 5), 14, (11, 1), 12, 22, (10, 7), 17, (10, 0), 13, (11, 2), 13, (11, 0), 18, 12, (10, 5),
            28, (11, 2), 12, 36, 17, (10, 5), 24, (11, 0), 18, 21, 38, (10, 0), 19, (10, 5), 20, 12, (10, 5), 28, (10, 5),
            14, (11, 1), 12, 22, 22
        ]
        expected_id_entries = [(0, 'x'), (1, 'miniloc'), (2, 'a'), (3, 'low'), (4, 'high'), (5, 'i'), (6, 'k'), (7, 'sort'), (8, 't'), (9, 'minloc'), (10, 'I'), (11, 'main')]
        expected_num_entries = [(0, '10'), (1, '1'), (2, '0')]

        f = open('scanner/test1.txt', 'r')
        token_seq, ids_table, nums_table = main.recognize_tokens(f)
        ids_entries = ids_table.get_entries()
        nums_entries = nums_table.get_entries()
        f.close()
        self.assertListEqual(token_seq, expected_token_seq_1, 'The token sequence does not equal the expected.')
        self.assertListEqual(ids_entries, expected_id_entries, 'Id entries does not equal the expected.')
        self.assertListEqual(nums_entries, expected_num_entries, 'Num entries does not equal the expected.')

    def test_recognize_reserved_words(self):
        """Test that the scanner detects every reserved word, despite of its capitalization.
        """

        expected_token_seq = [31, 32, 33, 34, 35, 36, 37, 38, 31, 32, 33 ]

        f = open('scanner/tests/text_files/test_res_words.txt', 'r')
        output = main.recognize_tokens(f)
        f.close()
        self.assertListEqual(output[0], expected_token_seq)

    def test_recognize_symbols(self):
        """Test that the scanner detects every symbol.
        """

        expected_token_seq = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

        f = open('scanner/tests/text_files/test_symbols.txt', 'r')
        output = main.recognize_tokens(f)
        f.close()
        self.assertListEqual(output[0], expected_token_seq)

    def test_outputs_bad_pseudotoken_msg(self):
        """Test that the scanner detects a bad pseudotoken and outputs the correct message.
        """

        expected_output = 'BadPseudoToken: Identifier or reserved word badly constructed.\n\tAt scanner/tests/text_files/test_bad_pseudotoken.txt:1'
        f = open('scanner/tests/text_files/test_bad_pseudotoken.txt', 'r')
        output = main.recognize_tokens(f)
        f.close()
        self.assertEqual(output, expected_output)

    def test_outputs_bad_number_msg(self):
        """Test that the scanner detects a bad number and outputs the correct message.
        """

        expected_output = 'BadNumber: Number literal badly constructed.\n\tAt scanner/tests/text_files/test_bad_number.txt:1'
        f = open('scanner/tests/text_files/test_bad_number.txt', 'r')
        output = main.recognize_tokens(f)
        f.close()
        self.assertEqual(output, expected_output)

    def test_outputs_bad_exclamation_msg(self):
        """Test that the scanner detects a bad number and outputs the correct message.
        """

        expected_output = 'UnexpectedChar: Unexpected "!" encountered.\n\tAt scanner/tests/text_files/test_bad_!.txt:1'
        f = open('scanner/tests/text_files/test_bad_!.txt', 'r')
        output = main.recognize_tokens(f)
        f.close()
        self.assertEqual(output, expected_output)

    def test_outputs_bad_compound_sym_msg(self):
        """Test that the scanner detects a bad compound symbol and outputs the correct message.
        """

        expected_output = 'BadCompoundSymbol: Compound symbol badly constructed.\n\tAt scanner/tests/text_files/test_bad_compound_sym.txt:1'
        f = open('scanner/tests/text_files/test_bad_compound_sym.txt', 'r')
        output = main.recognize_tokens(f)
        f.close()
        self.assertEqual(output, expected_output)

    def test_outputs_rare_sym_msg(self):
        """Test that the scanner detects a rare symbol and outputs the correct message.
        """

        expected_output = 'UnexpectedChar: A character that does not belong to the language\'s alphabet was encountered.\n\tAt scanner/tests/text_files/test_rare_sym.txt:1'
        f = open('scanner/tests/text_files/test_rare_sym.txt', 'r')
        output = main.recognize_tokens(f)
        f.close()
        self.assertEqual(output, expected_output)

    def test_outputs_non_closing_comment_msg(self):
        """Test that the scanner detects a non-closing comment and outputs the correct message.
        """

        expected_output = 'NonClosingComment: The EOF was reached with a non-closing comment.\n\tAt scanner/tests/text_files/test_non_closing_comment.txt:2'
        f = open('scanner/tests/text_files/test_non_closing_comment.txt', 'r')
        output = main.recognize_tokens(f)
        f.close()
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()