import unittest
from Classes.Calendar import Calendar
events = []
class Calendar_Test(unittest.TestCase):  
    def setUp(self):
        """Creates an instance of the calendar class for testing"""
        self.my_calendar = Calendar("Appointments", "Joe", events)
    def successfulAddEvent(self):
        self.events = self.my_calendar.addEvent("Infusion Appt")
        self.assertIn("Infusion Appt", self.my_calendar.events)
