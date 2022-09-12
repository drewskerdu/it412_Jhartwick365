import os.path
import shutil
import time
def addDataToBothDatabases(customer_data, db_conn):
    """This function will add data from the customer_data dictionary into our databases """
    # declare count control variable 
    count = 0
    # loop through every item in customer_data 
    for item in customer_data:
        # if there is no secondary phone provided in the dictionary entry, we wont provide it in our table 
        if customer_data[count]["secondary phone"] == "":
            # insert dictionary entry into the crm_data table 
            db_conn.executeQuery(f"INSERT INTO crm_data (f_name, l_name, Address, city, state, zip, company, primary_phone, email_address) VALUES ('{customer_data[count]['first name']}','{customer_data[count]['last name']}','{customer_data[count]['address']}','{customer_data[count]['city']}','{customer_data[count]['state']}','{customer_data[count]['zip code']}','{customer_data[count]['company']}','{customer_data[count]['primary phone']}','{customer_data[count]['email']}')")
            db_conn.conn.commit()
        else:
            # if the customer provided a secondary phone in the dictionary entry, we will provide it in our database entry. 
            # insert dictionary entry into the crm_data table
            db_conn.executeQuery(f"INSERT INTO crm_data (f_name, l_name, Address, city, state, zip, company, primary_phone, secondary_phone, email_address) VALUES ('{customer_data[count]['first name']}','{customer_data[count]['last name']}','{customer_data[count]['address']}','{customer_data[count]['city']}','{customer_data[count]['state']}','{customer_data[count]['zip code']}','{customer_data[count]['company']}','{customer_data[count]['primary phone']}','{customer_data[count]['secondary phone']}','{customer_data[count]['email']}')")
            db_conn.conn.commit()
        # insert dictionary entry into the mailings table 
        db_conn.executeQuery(f"INSERT INTO mailings (name, company, address) VALUES ('{customer_data[count]['first name']} {customer_data[count]['last name']}','{customer_data[count]['company']}','{customer_data[count]['address']}')")
        db_conn.conn.commit()
        count += 1
def getCustomerDataDictionary(fileLocation=''):
    """This function will generate the customer_data dictionary based on either a data file or the customer_export.txt"""
    # if the fileLocation attribute was not provided, we will assume that the user needs to import the data from the customer_export.txt file. 
    if fileLocation == '':
        fileLocation = "text_files/customer_export.txt"
    # declare empty customer_data list. This will be a list of dictionaries 
    customer_data = []
    # open the fileLocation in read mode 
    with open(fileLocation) as data:
        # declare count control variable 
        count = 0
        # loop through all the lines in the file location 
        for line in data:
            # in each line we will split the line up by ##|## since that is before and after each field
            temp_line = line.split("##|##")
            
            
            # the first line of customer_export.txt has field names like first name, last name company, etc. 
            # Therefore if count = 0, which is the first line in the file, we wont do anything 
            if count == 0:
                pass
            # otherwise if count doesnt equal 0, we will go into a while loop and assign some variable names based on the file 
            else:
                # declare place_counter control variable 
                place_counter = 0
                # while our placecounter variable is less than the length of our temp_line variable we will assign some names as the loop goes on 
                while place_counter < len(temp_line):
                    temp_line1 = temp_line[place_counter].strip("#")
                    # if the placecounter variable is 0, The first entry in a line in the customer_export.txt data file is first name. 
                    # Therefore we will assign the variable first name to temp_line1
                    if place_counter == 0:
                        first_name = temp_line1
                    # if the placecounter variable is 1, The second entry in a line in the customer_export.txt data file is last name. 
                    # Therefore we will assign the variable last name to temp_line1
                    elif place_counter == 1:
                        last_name = temp_line1
                    # if the placecounter variable is 2, The third entry in a line in the customer_export.txt data file is comany. 
                    # Therefore we will assign the variable company to temp_line1
                    elif place_counter == 2:
                        company = temp_line1
                    # if the placecounter variable is 3, The fourth entry in a line in the customer_export.txt data file is address 
                    # Therefore we will assign the variable address to temp_line1
                    elif place_counter == 3:
                        address = temp_line1
                    # if the placecounter variable is 4, The fifth entry in a line in the customer_export.txt data file is city. 
                    # Therefore we will assign the variable city to temp_line1
                    elif place_counter == 4:
                        city = temp_line1
                    # if the placecounter variable is 6, The seventh entry in a line in the customer_export.txt data file is state. 
                    # Therefore we will assign the variable state to temp_line1
                    elif place_counter == 6:
                        state = temp_line1
                    # if the placecounter variable is 7, The eighth entry in a line in the customer_export.txt data file is zip code. 
                    # Therefore we will assign the variable zip to temp_line1
                    elif place_counter == 7:
                        zip = temp_line1
                    # if the placecounter variable is 8, The ninth entry in a line in the customer_export.txt data file is primary phone. 
                    # Therefore we will assign the variable primary_phone to temp_line1
                    elif place_counter == 8:
                        primary_phone = temp_line1
                    # if the placecounter variable is 9, The tenth entry in a line in the customer_export.txt data file is secondary_phone 
                    # Therefore we will assign the variable secondary_phone to temp_line1
                    elif place_counter == 9:
                        secondary_phone = temp_line1
                    # if the placecounter variable is 10, The eleventh entry in a line in the customer_export.txt data file is email. 
                    # Therefore we will assign the variable email to temp_line1
                    elif place_counter == 10:
                        email = temp_line1
                    place_counter = place_counter + 1
                # check for duplicates
                item_duplicate = False
                # loop through every item in customer_data. If email address is already in customer_data we wont put the record in our dictionary 
                for item in range(0,len(customer_data)):
                    if email == customer_data[item]["email"]:
                        item_duplicate = True
                if item_duplicate == False:
                    customer_data.append({"first name" : first_name, "last name" : last_name, "company" : company, "address" : address, "city" : city, "state" : state, "zip code" : zip, "primary phone" : primary_phone, "secondary phone" : secondary_phone, "email" : email})    
            count += 1
    return customer_data
def getNewAddress():
    """This function will return a valid employee address """
    # while loop that will continue until the user enters a valid address
    while True:
        # prompt user for address input, and then pass the result into validateAddress
        address = input("Please enter the address on the record: ")
        address_ok = validateAddress(address)
        # if validateAddress comes back as false or is blank, we will say that it isnt properly formatted. Otherwise, we will return the address. 
        if address_ok == False or address == "":
            print("Address was not properly formatted. Please try again. ")
        else:
            return address
def getNewCity():
    """This function will return a valid city"""
    # while loop that will continue until the user enters a valid city
    while True:
        # prompt user for city input, and then pass the result into validateCity
        city = input("Please enter the city on the record: ").lower()
        city_ok = validateCity(city)
        # if validateCity comes back as false or is blank, we will say that it isnt properly formatted. Otherwise, we will return the city. 
        if city == "" or city_ok == False:
            print("City was not properly formatted. Please try again. ")
        else:
            return city
        
def getNewCompanyName():
    """This function will return the company name"""
    company_name = input("Please enter the company name on the record: (optional) Press enter to leave blank: ")
    return company_name
def getNewEmailAddress():
    """This function will return a valid email address"""
    # while loop that will continue until the user enters a valid email address
    while True:
        # prompt user for email address input, and then pass the result into validateEmail
        email_address = input("Please enter the email address on the record: (optional) Press enter to leave blank: ")
        email_ok = validateEmail(email_address)
        # if validateEmail comes back as True, we will return the email address. Otherwise, we will say that the email address was not properly formatted 
        if email_ok == True:
            return email_address
        else:
            print("Email address was not properly formatted. Please try again. ")
def getNewFirstName():
    """This function will return a valid first name"""
    # while loop that will continue until the user enters a valid email name
    while True:
        # prompt user for first name input, and then pass the result into validateName
        first_name = input("Please enter the first name on the record: ").lower()
        f_name_ok = validateFirstOrLastName(first_name)
        # if validateName comes back as True, we will return the first name. Otherwise, we will say that the name was not properly formatted 
        if f_name_ok == True:
            return first_name.title()
        else:
            print("First name was not properly formatted. Please try again. ")
def getNewLastName():
    """This function will return a valid last name"""
    # while loop that will continue until the user enters a valid name 
    while True:
        # prompt user for last name input, and then pass the result into validateName
        last_name = input("Please enter the last name on the record: ").lower()
        l_name_ok = validateFirstOrLastName(last_name)
        # if validateName comes back as True, we will return the last name. Otherwise, we will say that the name was not properly formatted 
        if l_name_ok == True:
            return last_name.title()
        else:
            print("Last name was not properly formatted. Please try again. ")
def getNewPhoneNumber(p_type):
    """This function will return a valid phone number"""
    # while loop that will continue until the user enters a valid email phone number
    while True:
        # if p_type is p for primary phone, we will prompt the user for primary phone input. Otherwise, we will prompt the user for seondary phone input. 
        if p_type == "p":
            phone_number = input("Please enter the primary phone number on the record in the format of NNN-NNN-NNNN: ")    
        else:
            phone_number = input("Please enter the secondary phone number on the record in the format of NNN-NNN-NNNN: (optional) Press enter to leave blank ")
        # then we will pass the phone number into validate phone number. 
        phone_ok = validatePhoneNumber(phone_number)
        # if p_type is P and the phone number is blank, we will say that it wasnt properly formatted
        if p_type == "p" and phone_number == "":
            print("Phone number was not properly formatted. Please try again.")
        # if phone_ok come back as true we will return the phone number. Otherwise, we will say that the phone number was not properly formatted. 
        elif phone_ok == True:
            return phone_number
        else:
            print("Phone number was not properly formatted. Please try again. ")
    
def getNewState():
    """This function will return a valid state"""
        # while loop that will continue until the user enters a valid state
    while True:
        # prompt user for state input, and then pass the result into validateState
        state = input("Please enter the state on the record in the form of 2 digits: ex. MI: ")
        state_ok = validateState(state)
        # if validateState comes back as false, we will say that the state was not properly formatted. Otherwise, we will return the state  
        if state_ok == False:
            print("State entered was not properly formatted. Please try again. ")  
        else:
            return state.upper()
def getNewZipCode():
    """This function will return a valid zip code"""
    # while loop that will continue until the user enters a valid zip code
    while True:
        # prompt user for zip code input, and then pass the result into validateZipCode
        zip_code = input("Please enter the zip code on the record in the form of 4 or 5 digits: ex. 1234 or 12345: ")
        zip_ok = validateZipCode(zip_code)
        # if validateZipCode comes back as false, we will say that the zip code was not properly formatted. Otherwise, we will return the zip code
        if zip_ok == False:
            print("Zip code was not properly formatted. Please try again. ")
        else:
            return zip_code

def validateAddress(address):
    """This function will validate the address entered"""
    # declare bad characters list 
    bad_chars = ["!", '"', "'", "@", "$", "%", "^", "&", "*", "_",  "=", "+", "<", ">",  "?", ";", "[", "]", "{", "}"]
    # declare control variable and for loop
    # loop through the bad characters list. If the character appears in address we will say that address_ok is false and return it. 
    address_ok = True
    for character in bad_chars:
        if character in address:
            address_ok = False
            break
    return address_ok
def validateCity(city):
    """This function will validate the city entered"""
    # declare allowed  characters list
    allowed_characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', "'", ' ']
    # declare control variable and for loop
    # loop through the allowed characters list. If the character doesn't appear in city, we will say that city_ok is false and return it.
    city_ok = True
    for character in city:
        if character not in allowed_characters:
            city_ok = False
            break
    return city_ok
def validateEmail(email):
    """This function will validate the email address entered"""
    # declare bad characters list 
    bad_chars = ['!', '"', "'", '#', '$', '%', '^', '&', '*', '(', ')',  '=', '+', ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\', " "]
    # declare control variable and for loop
    # loop through the characters in email If the character appears in the bad_chars list we will say that email_ok is false and return it. 
    email_ok = True
    for character in email:
        if character in bad_chars:
            email_ok = False
            break
    return email_ok

def validateFirstOrLastName(name):
    """This function will validate a first or last name"""
    # declare allowed characters list
    allowed_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "'", "-", " "]
    # declare control variable and for loop
    # loop through the allowed characters list. If the character appears in name, we will say that city_ok is true  and return it.
    name_ok = False
    for character in allowed_characters:
        if character in name:
            name_ok = True
            break
    return name_ok
def validatePhoneNumber(phone_number):
    """This function will validate the phone number entered"""
    # declare allowed characters list
    allowed_chars = ["0","1","2","3","4","5","6","7","8","9","0", "-"]
    # declare control variable and for loop
    # loop through the phone number. If the character appears in allowed chars, we will say that phone_ok is true and return it.
    phone_ok = True
    for character in phone_number:
        if character not in allowed_chars:
            phone_ok = False
            break
    return phone_ok
def validateRecordinCrm(db_conn, primary_phone):
    # call executeSelectQuery function that will select all the customer records and store it in result
    result = db_conn.executeSelectQuery("SELECT * FROM crm_data")
    record_ok = False
    # declare for loop. For every record in result. If the record_number matches the user input, then record_ok equals true and return it
    for record in result:
        if record["primary_phone"] == primary_phone:
            record_ok = True
            break
    return record_ok
def validateState(state):
    """This function will validate the state entered"""
    # set state_ok to false
    state_ok = False
    # if state is composed of alpha chars and the length of state if 2 characters we will return true. 
    if state.isalpha() and len(state) == 2:
        state_ok = True
    return state_ok
def validateZipCode(zip):
    """This function will validate the zip code entered"""
    # set zip_ok to false
    zip_ok = False
    # if zip is composed of digits 0-9 and the length of zip is either 4 of 5 we will return true
    if zip.isdigit() and (len(zip) == 4 or len(zip) == 5):
        zip_ok = True
    return zip_ok

def showCrm_dataDatabaseEntries(db_conn):
    """This function will show the data in the crm_data table. """
     # select all the entries from the crm_data table and store it in result 
    result = db_conn.executeSelectQuery("SELECT * FROM crm_data")
    # if there are no entries in result, we will say that there are no records in the database. They can press A to add a record or I to import data from a file. 
    if len(result) == 0:
        print("There are no records currenly in the database.\nFrom the main menu, press A to add a record. ")
    else:
        # for loop that will print out all the records in the database
        print("Here are all the records currenly in our crm_data database: ")
        for record in result:
            # if the record  hasnt been deleted yet we will print it out.
            if record["Deleted"] == "NO":
                print(f"\nCrm id: {record['crm_id']}\tFirst Name: {record['f_name']}\tLast Name: {record['l_name']}\tAddress: {record['Address']}\tCity: {record['city']}\tState: {record['state']}\tZip Code: {record['zip']}\nPrimary Phone: {record['primary_phone']}\tSecondary Phone: {record['secondary_phone']}\tEmail Address: {record['email_address']}")
    # print message saying that all the records have been displayed. 
    print("All the records are displayed. Returning to main menu.....")

def showMailingsDatabaseEntries(db_conn):
    """This function will show all the entries in the mailings database"""
    # select all the entries from the mailings table and store it in result 
    result = db_conn.executeSelectQuery("SELECT * FROM mailings")
    # if there are no entries in result, we will say that there are no records in the database. They can press A to add a record or I to import data from a file. 
    if len(result) == 0:
        print("There are no records currenly in the database.\nFrom the main menu, press A to add a record or I to import data from a file. ")
    else:
        # for loop that will print out all the records in the database
        print("Here are all the records currenly in our mailings database: ")
        for record in result:
            # if the record  hasnt been deleted yet we will print it out.
            if record["Deleted"] == "NO":
                print(f"Mail id: {record['mail_id']}\tName: {record['name']}\tCompany:: {record['company']}]\tAddress: {record['address']} ")
    # print message saying that all the records have been displayed. 
    print("All the records are displayed. Returning to main menu.....")


def trunicateBothDatabases(db_conn):
    """This function will truncate both database tables"""
    db_conn.executeQuery("TRUNCATE TABLE `python_projects`.`crm_data`")
    db_conn.executeQuery("TRUNCATE TABLE `python_projects`.`mailings`")

def writeCustomerDataCSV(customerData):
    """This function will take the customer_data dictionary and convert it to a csv file"""
    count = 0
    # code to backup my customers.csv file 
    if os.path.isfile("text_files/customers.csv"):
        shutil.copy2("text_files/customers.csv", "text_files/customers.csv.backup" + str(time.time()))
    # open customers.csv in write mode 
    with open("text_files/customers.csv", "w") as csvObj:
        # loop through every item in customerData
        for item in customerData:
            # if the count variable is 0, we will write the fields in the first row of the csv file plus the entry
            if count == 0:
                csvObj.write("First Name, Last Name, Company, Address, City, State, Zip Code, Primary Phone, Secondary Phone, Email\n")
                csvObj.write(f"{customerData[count]['first name']},{customerData[count]['last name']},{customerData[count]['company']},{customerData[count]['address']},{customerData[count]['city']},{customerData[count]['state']},{customerData[count]['zip code']},{customerData[count]['primary phone']}, {customerData[count]['secondary phone']}, {customerData[count]['email']}\n")
            else:
                # if count doesnt equal 0 we will just write the entry. 
                csvObj.write(f"{customerData[count]['first name']},{customerData[count]['last name']},{customerData[count]['company']},{customerData[count]['address']},{customerData[count]['city']},{customerData[count]['state']},{customerData[count]['zip code']},{customerData[count]['primary phone']}, {customerData[count]['secondary phone']}, {customerData[count]['email']}\n")

            count += 1

                

