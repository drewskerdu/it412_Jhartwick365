
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
    print("Press R to remove a current record in a database. ")
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
    # or if the answer is A we will prompt them to add a record to the databases
    elif answer == "a":
        print("You selected to add a record to our database. We will now prompt you for all the fields")
        # call the appropiate functions that will prompt the user for the various fields
        first_name = getNewFirstName()
        last_name = getNewLastName()
        company_name = getNewCompanyName()
        address = getNewAddress()
        city = getNewCity()
        state = getNewState()
        zip_code = getNewZipCode()
        p_type = "p"
        primary_phone = getNewPhoneNumber(p_type)
        p_type = "s"
        secondary_phone = getNewPhoneNumber(p_type)
        email = getNewEmailAddress()
        # start adding the records to the databases 
        # if the company name was left blank, we wont include it in our database query
        if company_name == "":
            db_conn.executeQuery(f"INSERT INTO crm_data (f_name, l_name, Address, city, state, zip, primary_phone,secondary_phone, email_address) VALUES ('{first_name}','{last_name}','{address}','{city}','{state}','{zip_code}','{primary_phone}','{secondary_phone}','{email}')")
            db_conn.executeQuery(f"INSERT INTO mailings (name, address) VALUES ('{first_name} {last_name}','{address}')")
            db_conn.conn.commit()
        # or if the company name and the secondary phone was left blank, we wont include it in our database query. 
        elif company_name == "" and secondary_phone == "":
            db_conn.executeQuery(f"INSERT INTO crm_data (f_name, l_name, Address, city, state, zip, primary_phone, email_address) VALUES ('{first_name}','{last_name}','{address}','{city}','{state}','{zip_code}','{primary_phone}','{email}')")
            db_conn.executeQuery(f"INSERT INTO mailings (name, company, address) VALUES ('{first_name} {last_name}','{company_name}','{address}')")
            db_conn.conn.commit()
        # or if the company name, secondary phone, and email were left blank, we wont include it in our database query. 
        elif company_name == "" and secondary_phone == "" and email == "":
            db_conn.executeQuery(f"INSERT INTO crm_data (f_name, l_name, Address, city, state, zip, primary_phone) VALUES ('{first_name}','{last_name}','{address}','{city}','{state}','{zip_code}','{primary_phone}')")
            db_conn.executeQuery(f"INSERT INTO mailings (name, company, address) VALUES ('{first_name} {last_name}','{company_name}','{address}')")
            db_conn.conn.commit()
        # or if secondary phone and email were left blank, we wont include it in our database query. 
        elif secondary_phone == "" and email == "":
            db_conn.executeQuery(f"INSERT INTO crm_data (f_name, l_name, Address, city, state, zip, company, primary_phone) VALUES ('{first_name}','{last_name}','{address}','{city}','{state}','{zip_code}','{company_name}','{primary_phone}')")
            db_conn.executeQuery(f"INSERT INTO mailings (name, company, address) VALUES ('{first_name} {last_name}','{company_name}','{address}')")
            db_conn.conn.commit()
        # or if the secondary phone was left blank, we wont include it in our database query. 
        elif secondary_phone == "":
            db_conn.executeQuery(f"INSERT INTO crm_data (f_name, l_name, Address, city, state, zip, company, primary_phone, email_address) VALUES ('{first_name}','{last_name}','{address}','{city}','{state}','{zip_code}','{company_name}','{primary_phone}','{email}')")
            db_conn.executeQuery(f"INSERT INTO mailings (name, company, address) VALUES ('{first_name} {last_name}','{company_name}','{address}')")
            db_conn.conn.commit()
        # or if the email was left blank, we wont include it in our database query. 
        elif email == "":
            db_conn.executeQuery(f"INSERT INTO crm_data (f_name, l_name, Address, city, state, zip, company, primary_phone, secondary_phone) VALUES ('{first_name}','{last_name}','{address}','{city}','{state}','{zip_code}',{company_name}'{primary_phone}','{secondary_phone}')")
            db_conn.executeQuery(f"INSERT INTO mailings (name, company, address) VALUES ('{first_name} {last_name}','{company_name}','{address}')")
            db_conn.conn.commit()
        # or if the user entered everything, we will include it in our database. 
        else:
            db_conn.executeQuery(f"INSERT INTO crm_data (f_name, l_name, Address, city, state, zip, company, primary_phone, secondary_phone, email) VALUES ('{first_name}','{last_name}','{address}','{city}','{state}','{zip_code}',{company_name}'{primary_phone}','{secondary_phone}','{email}')")
            db_conn.executeQuery(f"INSERT INTO mailings (name, company, address) VALUES ('{first_name} {last_name}','{company_name}','{address}')")
            db_conn.conn.commit()
        # tell the user that the record was sucessfully added too our databases 
        print("This record was sucessfully added to our databases. Returning to main menu..... ")
    # or if the user entered E we will prompt them for the various edit inputs
    elif answer == "e":
        # while loop that will continue until the user enters a valid database to modofy
        while True:
            # prompt the user for which database they woould like to modify data from 
            databaseChoice = input("Which database would you like to modify the record from? Press C for crm_data or Press M for mailings: ").lower()
            # If the user entered C or M, that is a valid choice and therefore we will break. 
            # Otherwise we will say that the choice wasnt formatted properly 
            if databaseChoice == "c" or databaseChoice == "m":
                break
            else:
                print("Your choice of databases was not properly formatted. Please try again. ")
        # If the user entered C for crm_data, we will prompt them for the various fields required to modify a record. 
        if databaseChoice == "c":
            # while loop that will continue until the user enters a valid phone number on the record to modify 
            while True:
                # prompt user for phone input
                phone_record = input("Please enter the primary phone number of the record you would like to modify: ")
                # call validateRecord function that will see if the phon number exists on a record. 
                record_ok = validateRecordinCrm(db_conn, phone_record)
                # if it comes back as true we will break. Otherwise, we will say that the phone number  was not properly formatted. 
                if record_ok == True:
                    break
                else:
                    print("Phone number was not properly formatted. Please try again. ")
            # while loop that will continue until the user enters a valid field to modify
            while True: 
                # prompt user for the field they would like to modify
                print("Please enter the field you would like to modify: ")
                field_choice = input("Press F for first name, L for last name, A for address, C for Company, P for primary phone, S for secondary phone or E for email address:  ").lower()
                # if the field choice is valid, we will break. Otherwise, we will say that the choice of field was not properly formatted. 
                if field_choice == "f" or field_choice == "l" or field_choice == "a" or field_choice == "c" or field_choice == "p" or field_choice == "s" or field_choice == "e":
                    break
                else:
                    print("Youe choice of field was not properly formatted. Please try again. ")
            # if the field choice was F, we will call the first name function and then update the record in crm_data
            if field_choice == "f":
                print("You have chosen to modify the first name. ")
                first_name = getNewFirstName()
                db_conn.executeQuery(f"UPDATE crm_data SET f_name='{first_name}' WHERE primary_phone='{phone_record}'")
                db_conn.conn.commit()
            # if the field choice was L, we will call the last name function and then update the record in crm_data
            elif field_choice == "l":
                print("You have chosen to modify the last name. ")
                last_name = getNewLastName()
                db_conn.executeQuery(f"UPDATE crm_data SET l_name='{last_name}' WHERE primary_phone='{phone_record}'")
                db_conn.conn.commit()
            # if the field choice was A, we will call the Address, City, State and Zip function and then update the record in crm_data
            elif field_choice == "a":
                print("You have chosen to modify the address. We will now prompt you for the various address fields: ")
                address = getNewAddress()
                city = getNewCity()
                state = getNewState()
                zip_code = getNewZipCode()
                db_conn.executeQuery(f"UPDATE crm_data SET Address='{address}' WHERE primary_phone='{phone_record}'")
                db_conn.executeQuery(f"UPDATE crm_data SET city='{city}' WHERE primary_phone='{phone_record}'")
                db_conn.executeQuery(f"UPDATE crm_data SET state='{state}' WHERE primary_phone='{phone_record}'")
                db_conn.executeQuery(f"UPDATE crm_data SET zip='{zip_code}' WHERE primary_phone='{phone_record}'")
                db_conn.conn.commit()
            # if the field choice was C, we will call the company function and then update the record in crm_data
            elif field_choice == "c":
                print("You have chosen to modify the company name. ")
                company_name = getNewCompanyName()
                db_conn.executeQuery(f"UPDATE crm_data SET company='{company_name}' WHERE primary_phone='{phone_record}'")
                db_conn.conn.commit()
            # if the field choice was P, we will call the phone number function and then update the record in crm_data
            elif field_choice == "p":
                print("You have selected to modify the primary phone number. ")
                # set p_type to p for primary and then pass the value into the phone number function
                p_type = "p"
                primary_phone = getNewPhoneNumber(p_type)
                db_conn.executeQuery(f"UPDATE crm_data SET primary_phone='{primary_phone}' WHERE primary_phone='{phone_record}'")
                db_conn.conn.commit()
            # if the field choice was S, we will call the phone number function and then update the record in crm_data
            elif field_choice == "s":
                print("You have selected to modify the secondary phone number. ")
                # set p_type to s for secondary and then pass the value into the phone number function
                p_type = "s"
                secondary_phone = getNewPhoneNumber(p_type)
                db_conn.executeQuery(f"UPDATE crm_data SET secondary_phone='{secondary_phone}' WHERE primary_phone='{phone_record}'")
                db_conn.conn.commit()
            # if the field choice was E, we will call the email address function and then update the record in crm_data
            elif field_choice == "e":
                print("You have selected to modify the email address. ")
                email = getNewEmailAddress()
                db_conn.executeQuery(f"UPDATE crm_data SET email_address='{email}' WHERE primary_phone='{phone_record}'")
                db_conn.conn.commit()
        elif databaseChoice == "m":
            pass
        print("This database record was sucessfully modifed. Returning to main menu......")
    elif answer == "r":
        pass
    elif answer == "q":
        print("Goodbye! Have a great day!")
        break
    else:
        print("Answer was not properly formatted. Please try again. ")