from Functions.my_functions import *
import unittest

class FunctionsTest(unittest.TestCase):
    """This class will test all the validation function in my_functions"""
    def testValidateVehicleMakePass(self):
        """This function will test the validate vehicle make function with passing values"""
        passingValues = ["Ford", "Toyota", "Chrysler"]
        for value in passingValues: 
            self.assertTrue(validateVehicleMake(value))
    def testValidateVehicleMakeFail(self):
        """This function will test the validate vehicle make function with failing values"""
        failingValues = ["Ford123", "Toyota$%^", "Chrysler!#%$!@"]
        for value in failingValues: 
            self.assertFalse(validateVehicleMake(value))
    def testValidateVehicleModelPass(self):
        """This function will test the validate vehicle model  function with passing values"""
        passingValues = ["Ford150", "Avalon", "Pacifcia"]
        for value in passingValues: 
            self.assertTrue(validateVehicleModel(value))
    def testValidateVehicleModelFail(self):
        """This function will test the validate vehicle model function with failing values"""
        failingValues = ["Ford150#1", "Avalon!@#$", "Pacifcia^&*("]
        for value in failingValues: 
            self.assertFalse(validateVehicleModel(value))
    def testValidateVehicleVINPass(self):
        """This function will test the validate vehicle VIN function with passing values"""
        passingValues = ["123456TE", "TYR321", "FTE345"]
        for value in passingValues: 
            self.assertTrue(validateVehicleVIN(value))
    def testValidateVehicleVINFail(self):
        """This function will test the validate vehicle VIN function with failing values"""
        failingValues = ["123456$#", "TYR321  ", "FTE345%"]
        for value in failingValues: 
            self.assertFalse(validateVehicleVIN(value))
    def testValidateOwnerNamePass(self):
        """This function will test the validate owners name function with passing values"""
        passingValues = ["hartwick, joseph", "petz, tom", "simko, michael"]
        for value in passingValues: 
            self.assertTrue(validateOwnerName(value))
    def testValidateOwnerNameFail(self):
        """This function will test the validate owner's name function with failing values"""
        failingValues = ["Hartwick!@$$#", "Petz!@#$$  ", "Simko%"]
        for value in failingValues: 
            self.assertFalse(validateOwnerName(value))
    def testsqlInjectionCheck(self):
        """This function will test my sql injection check function with both passing and failing values"""
        self.assertFalse(sql_injection_check("()>;"))
        self.assertTrue(sql_injection_check("12345"))