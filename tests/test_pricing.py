import unittest

from src.pricing import final_price


class PriceTests(unittest.TestCase):
    def test_ordinary_purchase(self):
        self.assertEqual(final_price(100, 20), 80)

    def test_discount_cannot_make_negative_price(self):
        self.assertEqual(final_price(10, 20), 0)


if __name__ == "__main__":
    unittest.main()
