
from Classes.Calendar import Calendar
from Classes.Event import Event
# declare events list

# instiutite an object of the calendar class called my_calendar
my_calendar = Calendar("", "", [])
# declare name while loop that will continue until the user enters a valid name 
while True:
    my_calendar.calendarName = input("Please enter the name of your calendar: ")
    # use the isalpha method on name. If its true we will break, otherwise we will continue
    if my_calendar.calendarName.isalpha():
        break
    else:
        print("Name was not properly formatted. Please try again.")
# declare owner while loop that will continue until the user enters a valid owner name 
while True:
    my_calendar.calendarOwner = input("Please enter your name or the owner of the calendar: ")
    # use the isalpha method on owner. If its true we will break, otherwise we will continue
    if my_calendar.calendarName.isalpha():
        break
    else:
        print("Calendar owner was not properly formatted. Please try again.")
# declare outer while loop that will continue until the user enters q
while True:
    # if the length of the events list is 0, we will not prompt the user to user to remove an event
    if len(my_calendar.events) > 0:
        answer = input("Would you like to add an event, or remove an event?\nEnter A for add, R for Remove or q to quit: ").lower()
    else:
        answer = input("Would you like to add an event?\nEnter A for add or q to quit: ").lower()

    # if the user enters A we will create a my_event object with empty attributes that will be filled up later. 
    if answer == "a":
        my_event = Event("", "", "", "")
        # declare name while loop that will continue until the user enters a valid event name 
        while True: 
            # prompt user for name 
            name = input("Please enter a name for your event: ")
            # make my_event.name equal to the name entered. Then we call the validate name method 
            my_event.name = name.lower()
            name_ok = my_event.validateName()
            # if the validateName method comes back as true we will break. Otherwise, the loop will continue. 
            if name_ok == True:
                break
       # declare date while loop that will continue until the user enters a valid event date  
        while True:
            # prompt user for date 
            date = input("Please enter the date of the event in the format of MM-DD-YYYY: ")
            # make my_event.date equal to the date entered. Then we call the validate date method 
            my_event.dateInfo = date
            date_ok = my_event.validateDateInfo()
            # if the validateDateInfo method comes back as true we will break. Otherwise, the loop will continue.
            if date_ok == True:
                break
        # declare date while loop that will continue until the user enters a valid event date
        while True:
            # prompt user for time 
            time = input("Please enter the time of your event: ")
            # make my_event.timeInfo equal to the time entered. Then we call the validate time method 
            my_event.timeInfo = time
            time_ok = my_event.validateTimeInfo()
            # if the validateTimeInfo method comes back as true we will break. Otherwise, the loop will continue.
            if time_ok == True:           
                break
        # declare event type while loop that will continue until the user enters a valid type of event
        while True:
            # prompt user for eventType
            EventType = input("Please enter if this is a 'single occurence', 'recurring' or a 'fixed number of meetings': ")
            # make my_event.type equal to the event type entered. Then we call the validate event type method 
            my_event.type = EventType
            type_ok = my_event.validateEventType()
            # if the validateEventType method comes back as true we will break. Otherwise, the loop will continue.
            if type_ok == True:                
                break
        # after all the event inputs are completed and validated, we will add the event to my_calendar
        print(f"{name} has been sucessfully added to your calendar.")
        my_calendar.addEvent(name)
    # the following block of code will be executed if the user enter R
    elif answer == "r":
        # declare remove event while loop that will continue until the user enters a valid event to remove
        while True: 
            # print out every event in the list and make it available for the user to remove 
            for item in my_calendar.events:
                print(item)
            remove_name = input("Which of these events would you like to remove? ")
            # if the user entered event is in the event list we will call the remove event method. Otherwise the loop will continue 
            if remove_name in my_calendar.events:
                my_calendar.removeEvent(remove_name)
                print(f"{remove_name} has been sucessfully removed from your calendar.")
                break
            else:
                print("I'm sorry that event is not in your calendar. Please try again.")
    # if the user enters Q we will break 
    elif answer == "q":
        break
    # if the users enters anything else, we will say that your answer was not properly formatted and for them to try again. 
    else:
        print("Your answer was not properly formatted. Please try again. ")

    

        

        





