from typing import Type
import leapYr
import unittest


class TestCase(unittest.TestCase):
    def test_leap(self):
        self.assertEqual(leapYr.leap_year(3), False)
    
    def test_leap(self):
        self.assertEqual(leapYr.leap_year(2004), True)
    
    def test_leap(self):
        self.assertEqual(leapYr.leap_year(400), True)
    
    def test_leap(self):
        self.assertEqual(leapYr.leap_year(2021), False)

    def test_leap(self):
        self.assertRaises(TypeError, leapYr.leap_year("hello"))
    
    def test_leap(self):
        self.assertEqual(leapYr.leap_year(400), False) #Should fail!






if __name__ == "__main__":
    unittest.main()