from Classes.Event import Event
import unittest

class Event_Test(unittest.TestCase):
    def setUp(self):
        """This method sets up 2 events: one with passing values and one with failing values"""
        self.my_event = Event("appt with lawyer", "8-16-2022", "04:00", "fixed number of meetings")
        self.my_event_fail = Event("Appt with lawyer 1200", "August 16th, 2022", "4 o clock", "meeting spreadout the month")
    def testValidateDateFail(self):
        """This method will test the validate date method with a failing value"""
        self.assertFalse(self.my_event_fail.validateDateInfo())  

    def testValidateDatePass(self):
        """This method will test the validate date method with a passing value"""
        self.assertTrue(self.my_event.validateDateInfo())

    def testValidateNameFail(self):
        """This method will test the validate name method with a failing value"""
        self.assertFalse(self.my_event_fail.validateName())
    def testValidateNamePass(self):
        """This method will test the validate name method with a passing value"""
        self.assertTrue(self.my_event.validateName())
    
    def testValidateTimeFail(self):
        """This method will test the validate time method with a failing value"""
        self.assertFalse(self.my_event_fail.validateTimeInfo())

    def testValidateTimePass(self):
        """This method will test the validate time method with a passing value"""
        self.assertTrue(self.my_event.validateTimeInfo())
    def testVaidateTypeFail(self):
        """This method will test the validate event type method with a failing value"""
        self.assertFalse(self.my_event_fail.validateEventType())
    def testValidateTypePass(self):
        """This method will test the validate event type method with a passing value"""
        self.assertTrue(self.my_event.validateEventType())
    
    