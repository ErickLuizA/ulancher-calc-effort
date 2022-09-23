import unittest
from datetime import datetime

from calc import handle_calc


class TestStringMethods(unittest.TestCase):

    def test_integer_input(self):
        self.assertEqual(handle_calc("15  "), 0.25)
        self.assertEqual(handle_calc("  20"), 0.33)
        self.assertEqual(handle_calc(" 30 "), 0.5)
        self.assertEqual(handle_calc("45"), 0.75)

    def test_start_time_input(self):
        self.assertEqual(handle_calc(
            "s=13:12   ", datetime(2022, 1, 1, 13, 42)), 0.5)
        self.assertEqual(handle_calc(
            "    s=13:12", datetime(2022, 1, 1, 14, 12)), 1)
        self.assertEqual(handle_calc(
            "  s=13:12  ", datetime(2022, 1, 1, 14, 42)), 1.5)
        self.assertEqual(handle_calc(
            "s=13:12", datetime(2022, 1, 1, 15, 12)), 2)

    def test_start_and_end_time_input(self):
        self.assertEqual(handle_calc("s=13:12 e=14:12   "), 1)
        self.assertEqual(handle_calc("   s=13:12 e=14:42"), 1.5)
        self.assertEqual(handle_calc("  s=13:12 e=15:12  "), 2)
        self.assertEqual(handle_calc("s=13:12 e=15:42"), 2.5)


if __name__ == '__main__':
    unittest.main()
