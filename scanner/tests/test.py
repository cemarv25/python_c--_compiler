import unittest
import main

class TestScanner(unittest.TestCase):
    def test_recognize_tokens(self):
        """Test that the scanner outputs the correct token sequence.
        """

        expected_token_seq_1 = [
            3, (30, 0), 16, (31, 0), 17, 9, 3, (30, 1), 14, 3, (30, 2), 16, 17, 10, 3, (30, 3), 10, 3, (30, 4), 15, 18, 3,
            (30, 5), 9, 3, (30, 0), 9, 3, (30, 6), 9, (30, 6), 25, (30, 3), 9, (30, 0), 25, (30, 2), 16, (30, 3), 17, 9, (30, 5),
            25, (30, 3), 11, (31, 1), 9, 6, 14, (30, 5), 21, (30, 4), 15, 18, 2, 14, (30, 2), 16, (30, 5), 17, 21, (30, 0), 15,
            18, (30, 0), 25, (30, 2), 16, (30, 5), 17, 9, (30, 6), 25, (30, 5), 9, 19, (30, 5), 25, (30, 5), 11, (31, 1), 9, 19,
            4, (30, 6), 9, 19, 5, (30, 7), 14, 3, (30, 2), 16, 17, 10, 3, (30, 3), 10, 3, (30, 4), 15, 18, 3, (30, 5), 9, 3,
            (30, 6), 9, (30, 5), 25, (30, 3), 9, 6, 14, (30, 5), 21, (30, 4), 12, (31, 1), 15, 18, 3, (30, 8), 9, (30, 6), 25,
            (30, 9), 14, (30, 2), 10, (30, 10), 10, (30, 4), 15, 9, (30, 8), 25, (30, 2), 16, (30, 6), 17, 9, (30, 2), 16,
            (30, 6), 17, 25, (30, 2), 16, (30, 5), 17, 9, (30, 2), 16, (30, 5), 17, 25, (30, 8), 9, (30, 5), 25, (30, 5), 11,
            (31, 1), 9, 19, 19, 5, (30, 11), 14, 5, 15, 18, 3, (30, 5), 9, (30, 5), 25, (31, 2), 9, 6, 14, (30, 5), 21, (31, 0),
            15, 18, 7, (30, 0), 16, (30, 5), 17, 9, (30, 5), 25, (30, 5), 11, (31, 1), 9, 19, (30, 7), 14, (30, 0), 10, (31, 2),
            10, (31, 0), 15, 9, (30, 5), 25, (31, 2), 9, 6, 14, (30, 5), 21, (31, 0), 15, 18, 8, (30, 0), 16, (30, 5), 17, 9,
            (30, 5), 25, (30, 5), 11, (31, 1), 9, 19, 19
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

        expected_token_seq = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3 ]

        f = open('scanner/tests/text_files/test_res_words.txt', 'r')
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