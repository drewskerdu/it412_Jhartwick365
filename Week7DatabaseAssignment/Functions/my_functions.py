
def getDescription():
    """This function will return a brief description of the vehicle"""
    # prompt user for input 
    while True:
        description = input("Please enter a brief description of the vehicle: ")
        check_ok = sql_injection_check(description)
        if check_ok == True:
            break
        else:
            print("Description was not properly formatted. Please try again. ")

    return description
def getOwnerName():
    """This function will return the name of the owner"""
    # while loop that will continue until the user enters a valid name
    while True:
        # prompt user for input 
        name = input("Please enter the name of the individual who sold the vehicle to our dealership(optional) Press enter to leave blank: ").lower()
        # since name is optional, if the user doesnt provide a name we will return ""
        if name == "":
            return ""
        # call our validateName function that will validate the owner name and return a booloan value: name_check
        name_check = validateOwnerName(name)
        # if name_check equals true we will return the name. Otherwise, we will prompt the user for the name again
        if name_check == True:
            return name.title()
        else:
            print("Owner name was not properly formatted. Please try again. ")
def getPricePaid():
    """This function will return the price the owner paid for the vehicle"""
    # while loop that will continue until the user enters a valid price
    while True:
        # try and except block. If a user doesnt enter a number, we will say that it was not properly formatted. 
        try:
            # prompt user for input
            pricePaid = float(input("Please enter the price the customer paid for the vehicle(optional) or enter 0 to leave it blank: "))
            # if the amount is 0 then we will return 0 back to our main program 
            # if the user enters a valid amount then we will break and return the value 
            if pricePaid == "0":
                return 0
            break
        except: 
            print("Price paid was not properly formatted. Please try again. ")
    return pricePaid
def getSalesPrice():
    """This function will return the sales price of the vehicle"""
    # while loop that will continue until the user enters a valid price
    while True: 
        # try and except block. If a user doesnt enter a number, we will say that it was not properly formatted. 
        try:
            # prompt user for input
            salesPrice = float(input("Please enter the sales price of the vehicle: "))
            # if the user enters a valid amount then we will break and return the value 
            break
        except: 
            print("Sales price was not properly formatted. Please try again. ")
    return salesPrice    

def getVehicleMake():
    """This function will return the valid make of the vehicle"""
    # while loop that will continue until the user enters a valid vehicle make 
    while True: 
        # prompt user for input
        make = input("Enter the make of the vehicle:  ")
        # call our validateMake function that will validate the vehicle make and return a booloan value: make_check
        make_check = validateVehicleMake(make)
        # if make_check equals true we will return the make. Otherwise, we will prompt the user for the make again
        if make_check == True:
            return make
        else:
            print("The make of the vehicle was not properly formatted. Please try again")
def getVehicleModel():
    """This function will return the valid model of the vehicle"""
    # while loop that will continue until the user enters a valid vehicle model
    while True:
        # prompt user for input
        model = input("Enter the model of the vehicle: ")
        # call our validateModel function that will validate the vehicle model and return a booloan value: model_check
        model_check = validateVehicleModel(model)
        # if model_check equals true we will return the model. Otherwise, we will prompt the user for the model again
        if model_check == True:
            return model
        else:
            print("Model of the vehicle was not properly formatted. Please try again. ")
def getVehicleVIN():
    """This function will return the valid VIN entered"""
    # while loop that will continue until the user enters a valid vehicle VIN
    while True:
        # prompt user for input
        vin = input("Enter the VIN model of the vehicle: ")
        # call our validateVIN function that will validate the vehicle VIN and return a booloan value: vin_check
        vin_check = validateVehicleVIN(vin)
        # if vin_check equals true we will return the vin. Otherwise, we will prompt the user for the vin again
        if vin_check == True:
            return vin
        else:
            print("VIN was not properly formatted. Please try again. ")


def showVehicles(car_db):
    """This function will show the current vehicles in our database"""
    # this line will select all the entries from the vehicle info table
    result = car_db.executeSelectQuery("SELECT * FROM vehicle_info")
    # if the result variable is 0, we would say that there are currenly no vehicles in the database. If there is > 1 vehicle we would print out all the vehicles 
    if len(result) == 0:
        print("There are no vehicles currenly in the database.\nFrom the main menu, press A to add a vehicle. ")
    else:
        print("Here are all the vehicles currenly in the database: ")
        # for loop that will print out all the records in the database
        for record in result:
            # if the record  hasnt been deleted yet we will print it out. Otherwise, we will do nothinh 
            if record["Deleted"] == "NO": 
                print(f"\nRecord number: {record['record_number']} ")
                print(f"Make: {record['vehicle_make']}")
                print(f"Model: {record['vehicle_model']}")
                print(f"Vin: {record['VIN_number']}")
                print(f"Owner Name: {record['owner_name']}")
                print(f"Price Paid: ${record['price_paid']}")
                print(f"Sales Price: ${record['sales_price']}")
                print(f"Vehicle Description: {record['vehicle_description']}\n")
            else:
                pass
def sql_injection_check(word):
    """This function will check for a sql injection"""
    bad_chars = ["(", ")", ">", ";"]
    word_ok = True
    for character in bad_chars:
        if character in word:
            word_ok = False
    return word_ok

def validateVehicleMake(make):
    """This function will validate the make entered"""
    # validation to make sure the vehicle is composed of Alphabet characters. Otherwise we return false
    if make.isalpha():
        return True
    else:
        return False

def validateVehicleModel(model):
    """This function will validate the model entered"""
    # declare disallowed characters list that we will loop through
    model_disallowed_characters = ['!', '"', '@', '#', '$', '%', '^', '*', '(', ')', '_', '=', '+', ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '?', '~', '|', '.']
    # control variable 
    model_check = True
    # for loop. For evey character in the disallowed_characters list, if the character appears in model, then model_check is false. Then we return model_check
    for character in model_disallowed_characters:
        if character in model:
            model_check = False
    return model_check
def validateOwnerName(name):
    """This function will validate the owner name entered"""
    # declare allowed characters list 
    allowed_characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", ",", ".", "'", "-"]
    # control variable 
    name_check = True
    # for loop. For every character in the name. If the character is not in allowed_characters, then name_check is false and we will return name_check 
    for character in name:
        if character not in allowed_characters:
            name_check = False
    return name_check

            
def validateVehicleVIN(vin):
    """This function will validate the VIN entered"""
    # if the VIN is composed of both letters and numbers, we will return true. Otherwise, we will return false 
    if vin.isalnum():
        return True
    else:
        return False






