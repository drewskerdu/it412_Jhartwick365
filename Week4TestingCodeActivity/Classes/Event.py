class Event():
    """This class stores a event currenly being executed in our program """
    def __init__(self, name, dateInfo, timeInfo, type):
        """This method initalizes the Event class's attributes """
        self.name = name
        self.dateInfo = dateInfo
        self.timeInfo = timeInfo
        self.type = type
    def validateDateInfo(self):
        """This method is called to validate an event's date"""
        date_ok = True
        # for loop that will loop through the characters in the date and will set dateOk to false if it finds anything other than numbers or a -
        for character in self.dateInfo:
            if character == "0" or character == "1" or character == "2" or character == "3" or character == "4" or character == "5" or character == "6" or character == "7" or character == "8" or character == "9" or character == "10" or character == "-":
                pass
            else:
                date_ok = False
        # If date_ok is false we will say that the date was not properly formatted and return false. Otherwise, we will return true
        if date_ok == False:
            print("Date was not properly formatted. Please try again")
            return False
        else:
            return True
    def validateEventType(self):
        """This method is called to validate the type of event"""
        # if the event type is anything other than single occurance recurring or a fixed number of meetings we will return false. Otherwise we return true 
        if self.type == "single occurrence" or self.type == "recurring" or self.type == "fixed number of meetings":
            return True
        else:
            print("Event type was not properly formatted. Please try again")
            return False
    
    def validateName(self):
        """This method is called to validate a event's name"""
        # declare name_ok control variable and set it to true. It will turn false if the for loop finds anything others than letters or spaces in the name
        name_ok = True
        # for loop that will loop through the characters in the name. If its not a letter or a space name ok will become false 
        for character in self.name:
            if character == "a" or character == "b" or character == "c" or character == "d" or character == "e" or character == "f" or character == "g" or character == "h" or character == "i" or character == "j" or character == "k" or character == "l" or character == "m" or character == "n" or character == "o" or character == "p"  or character == "q" or character == "r" or character == "s" or character == "t" or character == "u" or character == "v" or character == "w" or character == "x" or character == "y" or character == "z" or character == " ":
                pass
            else:
                name_ok = False
        # if name_ok is true we will return true back into our main program. Otherwise we will return false 
        if name_ok == True:
            return True
        else:
            print("Name was not properly formatted. Please try again")
            return False
    
    
    def validateTimeInfo(self):
        """This method is called to validate an event time"""
        
        time_ok = True
        # for loop that will loop through the characters in the time. If it finds anything other than numbers or a :, time_ok will become false
        for character in self.timeInfo:
            if character == "0" or character == "1" or character == "2" or character == "3" or character == "4" or character == "5" or character == "6" or character == "7" or character == "8" or character == "9" or character == "10" or character == ":":
                pass
            else:
                time_ok = False
        # if time_ok is false we will return false. Otherwise, we will return true. 
        if time_ok == False:
            print("Time was not properly formatted. Please try again")
            return False
        else:
            return True
    
    
