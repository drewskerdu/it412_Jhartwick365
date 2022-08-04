
from Classes.Calendar import Calendar
from Classes.Event import Event

events = ["Joes shitshow"]
my_calendar = Calendar("", "", events)

while True:
    my_calendar.calendarName = input("Please enter the name of your calendar: ")
    if my_calendar.calendarName.isalpha():
        break
    else:
        print("Name was not properly formatted. Please try again.")
while True:
    my_calendar.calendarOwner = input("Please enter your name or thw owner of the calendar: ")
    if my_calendar.calendarName.isalpha():
        break
    else:
        print("Calendar owner was not properly formatted. Please try again.")
while True:
    if len(events) > 0:
        answer = input("Would you like to add an event, or remove an event?\nEnter A for add, R for Remove or q to quit: ").lower()
    else:
        answer = input("Would you like to add an event?\nEnter A for add or q to quit: ").lower()


    if answer == "a":
        my_event = Event("", "", "", "")
        while True: 
            name = input("Please enter a name for your event: ")
            my_event.name = name.lower()
            name_ok = my_event.validateName()
            if name_ok == True:
                break
        while True:
            date = input("Please enter the date of the event in the format of MM-DD-YYYY: ")
            my_event.dateInfo = date
            date_ok = my_event.validateDateInfo()
            if date_ok == True:
                break
        while True:
            time = input("Please enter the time of your event: ")
            my_event.timeInfo = time
            time_ok = my_event.validateTimeInfo()
            if time_ok == True:           
                break

        while True:
            EventType = input("Please enter if this is a 'single occurence', 'recurring' or a 'fixed number of meetings': ")
            my_event.type = EventType
            type_ok = my_event.validateEventType()
            if type_ok == True:                
                break
        events = my_calendar.addEvent(name)
    elif answer == "r":
        while True: 
            for item in events:
                print(item)
            remove_name = input("Which of these events would you like to remove? ")
            if remove_name in events:
                events =  my_calendar.removeEvent(remove_name)
                break
            else:
                print("I'm sorry that event is not in your calendar. Please try again.")
    elif answer == "q":
        break
    else:
        print("Your answer was not properly formatted. Please try again. ")

    

        

        





