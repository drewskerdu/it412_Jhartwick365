from Classes.Calendar import *
import unittest
events = []
class CalendarTest(unittest.TestCase):  
    def setUp(self):
        """Creates an instance of the calendar class for testing"""
        self.my_calendar = Calendar("Appointments", "Joe", events)
    def testAddEvent(self):
        """This method tests adding an event to the calendar"""
        self.my_calendar.addEvent("Infusion Appt")
        self.assertIn("Infusion Appt", self.my_calendar.events)
    def testRemoveEvent(self):
        """This method tests removing an event to the calendar"""
        self.my_calendar.removeEvent("Infusion Appt")
        self.assertNotIn("Infusion Appt", self.my_calendar.events)


    

