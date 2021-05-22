import leapYr
import unittest


class TestCase(unittest.TestCase):
    def test_leap(self):
        self.assertEqual(leapYr.leap_year(2000), True)


if __name__ == "__main__":
    unittest.main()