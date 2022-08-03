from Functions.my_functions import *
# declare while loop that will continue until the user enters a valid month 
while True:
    month = int(input("Please enter the current month: (1-12) "))
    # call validate month function that will validate the month entered
    month_ok = validateMonth(month)
    # if the month entered was formatted properly we will break, otherwise the loop will continue 
    if month_ok == True:
        break
    else:
        print("Month was not properly formatted. Please try again. ")
        
# declare while loop that will continue until the user enters a valid day
while True:
    day = int(input("Please enter the current day: (1-31) "))
    # call validate day function that will validate the day entered
    day_ok = validateDay(day)
    # if the day entered was formatted properly we will break, otherwise the loop will continue 
    if day_ok == True:
        break
    else:
        print("Day was not properly formatted. Please try again. ")
# declare while loop that will continue until the user enters a valid year
while True:
    year = int(input("Please enter the current year: (YYYY)"))
    # call validate year function that will validate the year entered
    year_ok = validateDay(day)
    # if the year entered was formatted properly we will break, otherwise the loop will continue 
    if year_ok == True:
        break
    else:
        print("Year was not properly formatted. Please try again. ")
# call getformatteddate function that will return the date formatted well. 
date = getFormattedDate(month, day, year)
print("The current date is: " + date)