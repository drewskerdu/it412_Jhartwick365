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
def getNewFirstName():
    while True:
        first_name = input("Please enter the first name on the record: ").lower()
        f_name_ok = validateFirstOrLastName(first_name)
        if f_name_ok == True:
            break
        else:
            print("First name was not properly formatted. Please try again. ")
def validateFirstOrLastName(name):
    allowed_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "'", "-", " "]
    name_ok = False
    for character in allowed_characters:
        if character in name:
            name_ok = True

    return name_ok 

def showCrm_dataDatabaseEntries(db_conn):
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

                

