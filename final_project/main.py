
# import my functions, classes json, and backup files
from Functions.my_functions import *
from Classes.database_access import *
import json
import os.path
import shutil
import time
# connect to my database
db_conn = DB_Connect('root', '', 'python_projects')
# check to see if customers.json exists. If it doesnt, we insert data from the customer_export.txt into our databases and our .csv and json file. 
# try opening customers.json in read mode. If the file doesnt exist, we will create along with inserting data into our databases. 
try:
    with open("text_files/customers.json") as json_obj:
        pass
except FileNotFoundError:
    # call our get customer dictionary that will return the customer_data dictionary based off of the customer_export.txt text file. 
    customer_data = getCustomerDataDictionary()
    
    # once the customer_data we will use json.dump to dump it into customers.json
    with open("text_files/customers.json","w") as json_obj:
        json.dump(customer_data, json_obj)
    # We will also write it to the csv file, then add the data to both databases 
    writeCustomerDataCSV(customer_data)
    addDataToBothDatabases(customer_data, db_conn)
# print menu gretting     
print("Welcome to the customer data manager for Joe's Crab shack! ")

# declare outer while loop that will continue until the user enters q for quit 
while True:    
    # prompt user for different menu bar options. 
    print("Press I to import data from a new customer export data file.")
    print("Press S to show data currenly in a database")
    print("Press A to add a record to the databases. ")
    print("Press E to edit a record currenly in a database. ")
    print("Press Q to quit the program. ")
    # store the answer the user provides in the variable answer 
    answer = input().lower()
    # if the user enters I for import data from a file, we will prompt the user for the file location. Then add the file data to both databases, the csv file, and the json file. 
    if answer == "i":
        # while loop that will continue until the user enters a valid file location
        while True:
            # try and except block. If the file location is a valid location, we will break. Otherwise, we will say that the file location was not formatted properly. 
            try:
                # prompt user for input
                file = input("Please enter the file location where you would like to import data from: ")
                # attempt to open the file in read only mode. If it throws an error, we will say that the file location could not be found. 
                with open(file) as fileObj:
                    pass
                break
            except FileNotFoundError:
                print("This file location could not be found or doesn't exist. Please try again. ")
        # once the data file is valid, we will trunicate both databases before adding the file to our databases. 
        trunicateBothDatabases(db_conn)
        # back up customers.json file before we overwrite it 
        if os.path.isfile("text_files/customers.json"):
            shutil.copy2("text_files/customers.json", "text_files/customers.json.backup" + str(time.time()))
        # generate customer data dictionary using a function
        customer_data = getCustomerDataDictionary(file)
        # add data to both databases using that function. 
        addDataToBothDatabases(customer_data, db_conn)
        # we will write our customer_data.csv file based on the customer_data dictionary. 
        writeCustomerDataCSV(customer_data)
        # we will dump the customer_data dictionary into the customers.json file
        with open("text_files/customers.json", "w") as jsonObj:
            json.dump(customer_data, jsonObj)
        # notify the user that the file was sucessfully added to the databases and tech files. 
        print("This data file was sucessfully added to our databases and tech files. Returning to main menu.....")
    # if the user entered s for show data currenly in a database we will prompt them for which database they would like to show data from and then display the data 
    elif answer == "s":
        # while loop that continues until the user enters a valid database
        while True:
            # prompt user for which database they would like to show data from  
            databaseChoice = input("Which database would you like to show data from? Press C to show data from crm_data or press M to show data for mailings. ").lower()
            # if they chose M for the mailings database, we will call the function to show data from the mailings database and then break out of the loop. 
            if databaseChoice == "m":
                showMailingsDatabaseEntries(db_conn)
                break
            # if they chose C for the crm_data database, we will call the function to show data from the crm_data database and then break out of the loop
            elif databaseChoice == "c":
                showCrm_dataDatabaseEntries(db_conn)
                break
            # if the user entered anything other than C or M we will say that it wasnt formatted properly. 
            else:
                print("Your database choice wasn't formatted properly. Please try again. ")
    elif answer == "a":
        print("You selected to add a record to our database. We will now prompt you for all the fields")
        first_name = getNewFirstName()
        
    elif answer == "e":
        pass
    elif answer == "q":
        print("Goodbye! Have a great day!")
        break
    else:
        print("Answer was not properly formatted. Please try again. ")