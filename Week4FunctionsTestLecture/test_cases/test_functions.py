import unittest
from Functions.function_library import *

class NamePartTestCase(unittest.TestCase):
    """Tests for functions in the functions_library file"""

    def test_valid_name_part(self):
        """Heres is a test I think should work"""
        valid_names_to_test = ["Joe", "joe", " Joe", " joe", "joe"]
        
        for name in valid_names_to_test:
            self.assertTrue(validate_name_part(name))


    def test_invalid_name_part(self):
        """Heres is a test I think shouldn't work"""
        invalid_names_to_test = ["'Joe'", "123", " Joe 123", "#joe", "   "]
        
        for name in invalid_names_to_test:
            self.assertFalse(validate_name_part(name))
