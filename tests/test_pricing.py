import unittest
from src.pricing import final_price
class TestOrdinary(unittest.TestCase):
    def test_ordinary(self):
        self.assertEqual(final_price(100,20),80)
