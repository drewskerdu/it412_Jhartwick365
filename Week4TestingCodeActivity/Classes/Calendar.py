


class Calendar():
    """This class stores various calendar event, along with the name of the calendar and the calendar owner"""
    def __init__(self, calendarName, calendarOwner, events):
        """This constructor intalizes the calendar class's attributes """
        self.calendarName = calendarName
        self.calendarOwner = calendarOwner
        self.events = events
    def addEvent(self, eventAdd):
        """This method is executed when a user adds an event to their calendar """
        self.events.append(eventAdd)
        return self.events
    def removeEvent(self, eventRemove):
        """This method is executed when a user removes an event to their calendar """
        if eventRemove in self.events:
            self.events.remove(eventRemove)
        return self.events
