import unittest
from data_structures.id_generator import IdGenerator

class TestIdGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = IdGenerator()
    
    def test_sequential_ids(self):
        """Test that the ids generated are sequential
        """

        expected_output = [0, 1, 2, 3, 4]
        output = [self.generator.next() for _ in range(5)]
        self.assertListEqual(output, expected_output)

    def test_starting_id(self):
        """Test that if a starting_id is passed, the first generated id is that number
        """

        expected_output = 10
        self.generator = IdGenerator(10)
        output = self.generator.next()
        self.assertEqual(output, expected_output)

    def test_count(self):
        """Test that the count is the correct amount of ids generated
        """

        expected_output = 10
        [self.generator.next() for _ in range(10)]
        output = self.generator.count
        self.assertEqual(output, expected_output)
