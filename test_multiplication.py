from unittest import TestCase
from multiplication1 import multiplication

class TestMultiplication(TestCase):
    def test_multiplication(self):
        self.assertEqual(multiplication(3,4),12)
    def test_string_a_3(self):
        self.assertEqual(multiplication('a',2),'aa')
