import unittest

def leap_year(chosen_year):
    # while True:
    #     chosen_year = int(input("Hello! Please enter a positive number to determine if it is a leap year: "))
    #     if chosen_year >= 0:
    #         break

    if chosen_year % 4 != 0:
        print("Your year is not a leap year!")
        return False
    else:
        if chosen_year % 100 == 0:
            if chosen_year % 400 == 0:
                print("Your year is a leap year!")
                return True
            else:
                print("Your year is not a leap year!")
                return False
        else:
            print("Your year is a leap year!")
            return True



class TestCase(unittest.TestCase):
    def test_leap1(self):
        self.assertEqual(leap_year(3), False)
    
    def test_leap2(self):
        self.assertEqual(leap_year(2004), True)
    
    def test_leap3(self):
        self.assertEqual(leap_year(400), True)
    
    def test_leap4(self):
        self.assertEqual(leap_year(2021), False)

    def test_leap5(self):
        self.assertRaises(TypeError, leap_year("hello"))
    
    def test_leap6(self):
        self.assertEqual(leap_year(400), False) #Should fail!






if __name__ == "__main__":
    unittest.main()