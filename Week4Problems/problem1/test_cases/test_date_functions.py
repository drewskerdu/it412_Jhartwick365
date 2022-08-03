# import unittest and functions 
import unittest
from Functions.my_functions import *
# declare date test class
class DateTestCase(unittest.TestCase):
    """Test the functions in the my_functions file"""
    def test_valid_month(self):
        self.assertTrue(validateMonth(4))
    def test_invalid_month(self):
        self.assertFalse(validateMonth(400))
    def test_valid_day(self):
        self.assertTrue(validateDay(7))
    def test_invalid_day(self):
        self.assertFalse(validateDay(700))
    def test_valid_year(self):
        self.assertTrue(validateYear(2022))
    def test_invalid_year(self):
        self.assertFalse(validateYear(7000))