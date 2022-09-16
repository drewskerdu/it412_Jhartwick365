from Functions.my_functions import *
import unittest

class functionsTest(unittest.TestCase):
    """This class will test all of the validation functon in myFunctions"""
    def testValidateAddressFail(self):
        """This function will test some values that will come back as false in the validateAddress function"""
        fail_test = ["#2746 &Nita", "@22358 &yman", "!6543 ^Freaky"]
        for test in fail_test:
            self.assertFalse(validateAddress(test))
    def testValidateAddressPass(self):
        """This function will test some values that will come back as true in the validateAddress function"""
        pass_test = ["2746 Nita", "22358 Cyman", "6543 Freaky"]
        for test in pass_test:
            self.assertTrue(validateAddress(test))
    def testValidateCityFail(self):
        """This function will test some values that will come back as false in the validateCity function"""
        fail_test = ["#warren", "&detroit", "#sterling heights"]
        for test in fail_test:
            self.assertFalse(validateCity(test))
    def testValidateCityPass(self):
        """This function will test some values that will come back as True in the validateCity function"""
        pass_test = ["warren", "detroit", "sterling heights"]
        for test in pass_test:
            self.assertTrue(validateCity(test))
    def testValidateEmailFail(self):
        """This function will test some values that will come back as false in the validateEmail function"""
        fail_test = ["#$%#@gmail.com", "^%$#!@walshcollege.edu", "$#@!#$#@!T%&&^@yahoo.com"]
        for test in fail_test:
            self.assertFalse(validateEmail(test))
    def testValidateEmailPass(self):
        """This function will test some values that will come back as true in the validateEmail function"""
        fail_test = ["bob1@gmail.com", "tpetz@walshcollege.edu", "hartwickjoseph821@yahoo.com"]
        for test in fail_test:
            self.assertTrue(validateEmail(test))
    def testValidateFirstOrLastNameFail(self):
        """This function will test some values that will come back as false in the validateFirstOrLastName function"""
        fail_test = ["joe the 3rd", "tom petz!!", "alvin toma the 1st"]
        for test in fail_test:
            self.assertFalse(validateFirstOrLastName(test))
    def testValidateFirstOrLastNamePass(self):
        """This function will test some values that will come back as true in the validateFirstOrLastName function"""
        pass_test = ["joe", "tom", "alvin"]
        for test in pass_test:
            self.assertTrue(validateFirstOrLastName(test))
    def testValidatePhoneNumberFail(self):
        """This function will test some values that will come back as false in the validatePhoneNumber function"""
        fail_test = ["fiveeightsix", "twotwotwo", "twooneonefive"]
        for test in fail_test:
            self.assertFalse(validatePhoneNumber(test))
    def testValidatePhoneNumberPass(self):
        """This function will test some values that will come back as true in the validatePhoneNumber function"""
        pass_test = ["586-222-2115", "248-229-0663", "586-222-7661"]
        for test in pass_test:
            self.assertTrue(validatePhoneNumber(test))
    def testValidateStateFail(self):
        """This function will test some values that will come back as false in the validateState function"""
        fail_test = ["michigan", "ohio", "california"]
        for test in fail_test:
            self.assertFalse(validateState(test))   
    def testValidateStatePass(self):
        """This function will test some values that will come back as true in the validateState function"""
        pass_test = ["MI", "OH", "CA"]
        for test in pass_test:
            self.assertTrue(validateState(test))
    def testValidateZipCodeFail(self):
        """This function will test some values that will come back as false in the validateZipCode function"""
        fail_test = ["#48091", "44870!", "48092$"]
        for test in fail_test:
            self.assertFalse(validateZipCode(test))
    def testValidateZipCodePass(self):
        """This function will test some values that will come back as true in the validateZipCode function"""
        pass_test = ["48091", "44870", "48092"]
        for test in pass_test:
            self.assertTrue(validateZipCode(test))          

        