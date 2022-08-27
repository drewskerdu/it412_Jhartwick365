
from Classes.database_access import DB_Connect
from Functions.my_functions import *

# declare DB_Connect object that will connect to the database
car_db = DB_Connect('root', '', 'car_dealership_records')

print("Welcome to the vehicle manager for Joe's Vehicles!")
# declare outer while loop 
while True:
    # give the user a menubar with a list of options to choose from 
    print("Press S to show all vehicles currenly in the database.")
    print("Press A to add a new vehicle to the database. ")
    print("Press E to edit a vehicle.")
    print("Press R to remove a vehicle.")
    print("Press Q to quit the program. ")
    print("What would you like to do?")
    # gather input 
    answer = input().lower()
    
             
    # if the user entered S to show all vehicles, we will call the show vehicles function and pass in our database 
    if answer == "s":
        showVehicles(car_db)
    # if the user entered A to add a vehicle, we will call the various input vehicle functions that will validate and return the value back into our main program 
    elif answer == "a":
        make = getVehicleMake()
        model = getVehicleModel()
        vin = getVehicleVIN()
        name = getOwnerName()
        pricePaid = getPricePaid()
        salesPrice = getSalesPrice()
        description = getDescription()
        # if the user didnt provide a owner name nad a price paid then we wont include those in out database table entry
        if name == "" and pricePaid == 0:
            # call the executeQuery function to insert a new record into our database table and then commit those changes. 
            car_db.executeQuery(f"INSERT INTO vehicle_info (vehicle_make, vehicle_model, VIN_number, sales_price, vehicle_description) VALUES ('{make}', '{model}', '{vin}', '{salesPrice}', '{description}'  ) ")
            car_db.conn.commit()
        # if the user didnt provide only a owner name, then we will not include it in our database table entry
        elif name == "":
            # call the executeQuery function to insert a new record into our database table and then commit those changes. 
            car_db.executeQuery(f"INSERT INTO vehicle_info (vehicle_make, vehicle_model, VIN_number, price_paid, sales_price, vehicle_description) VALUES ('{make}', '{model}', '{vin}', '{pricePaid}', '{salesPrice}', '{description}'  ) ")
            car_db.conn.commit()
        # if the user didnt provide only the price paid, then we will not include it in our database table entry
        elif pricePaid == 0:
            # call the executeQuery function to insert a new record into our database table and then commit those changes.
            car_db.executeQuery(f"INSERT INTO vehicle_info (vehicle_make, vehicle_model, VIN_number, owner_name, sales_price, vehicle_description) VALUES ('{make}', '{model}', '{vin}','{name}', '{salesPrice}', '{description}'  ) ")
            car_db.conn.commit()
        # if the user provided all the entries, then we will include all of them in our entries and commit those changes
        else:
            car_db.executeQuery(f"INSERT INTO vehicle_info (vehicle_make, vehicle_model, VIN_number, owner_name, price_paid, sales_price, vehicle_description) VALUES ('{make}', '{model}', '{vin}','{name}', '{pricePaid}', '{salesPrice}', '{description}'  ) ")
            car_db.conn.commit()
        # tell the user that the record was sucessfully added to the database
        print("\nThis vehicle was sucessfully added to our database. Returning to main menu....\n")
    # if the user entered E for edit the following block of code will be executed 
    elif answer == "e":
        # declare while loop that will continue until the user enters a valid record number to modify
        while True:
            # try and except block that will handle an error if the user enters anything other than a number 
            try:
                # call the show vehicles function that will show all the vehicles in the database
                showVehicles(car_db)
                # prompt the user for the record number they would like to modify 
                record_number = int(input("Enter the record number you would like to edit: "))
                # call executeSelectQuery function that will select all the vehicles and store it in result
                result = car_db.executeSelectQuery("SELECT * FROM vehicle_info")
                record_ok = False
                # declare for loop. For every record in result. If the record_number matches the user input, then record_ok equals true 
                for record in result:
                    if record["record_number"] == record_number:
                        record_ok = True
                        break
                # if record_ok equals true we will break out of the loop. otherwise we will say that the record was not properly formatted. 
                if record_ok == True:
                    break 
                else:
                    print("Record number was not properly formatted or doesnt exist. Please try again. ")
            except:
                print("Record number was not properly formatted or doesnt exist. Please try again. ")
        # declare while loop that will continue until the user enters a valid field to modify 
        while True:
            # prompt the user for the field they would like to modify. 
            field = input("What field would you like to edit for this record? Enter Make, Model, VIN, Name, Price Paid, Sales Price or description. ").lower()
            # if the user entered make as the field we will call the vehicleMake function then run an update query and commit the changes 
            if field == "make":
                make = getVehicleMake()
                car_db.executeQuery(f"UPDATE vehicle_info SET vehicle_make='{make}' WHERE record_number='{record_number}'")
                car_db.conn.commit()
                break
            # if the user entered model as the field we will call the vehicleModel function then run an update query and commit the changes
            elif field == "model":
                model = getVehicleModel()
                car_db.executeQuery(f"UPDATE vehicle_info SET vehicle_model='{model}' WHERE record_number='{record_number}'")
                car_db.conn.commit()
                break
            # if the user entered VIN as the field we will call the vehicleVIN function then run an update query and commit the changes
            elif field == "vin":
                vin = getVehicleVIN()
                car_db.executeQuery(f"UPDATE vehicle_info SET VIN_number='{vin}' WHERE record_number='{record_number}'")
                car_db.conn.commit()
                break
            # if the user entered name as the field we will call the ownerName function then run an update query and commit the changes
            elif field == "name":
                name = getOwnerName()
                car_db.executeQuery(f"UPDATE vehicle_info SET owner_name='{name}' WHERE record_number='{record_number}'")
                car_db.conn.commit()
                break
            # if the user entered price paid as the field we will call the pricePaid function then run an update query and commit the changes
            elif field == "price paid":
                pricePaid = getPricePaid()
                car_db.executeQuery(f"UPDATE vehicle_info SET price_paid='{pricePaid}' WHERE record_number='{record_number}'")
                car_db.conn.commit()
                break
            # if the user entered sales price as the field we will call the salesPrice function then run an update query and commit the changes
            elif field == "sales price":
                salesPrice = getSalesPrice()
                car_db.executeQuery(f"UPDATE vehicle_info SET sales_price='{salesPrice}' WHERE record_number='{record_number}'")
                car_db.conn.commit()
                break
            # if the user entered description as the field we will call the description function then run an update query and commit the changes
            elif field == "description":
                description = getDescription()
                car_db.executeQuery(f"UPDATE vehicle_info SET vehicle_description='{description}' WHERE record_number='{record_number}'")
                car_db.conn.commit()
                break
            # if the user entered anything else, we will say that it isn't properly formatted, then we will prompt the user again. 
            else:
                print("Field entered was not properly formatted. Please try again.")
        # tell the user that the record was sucessfully edited          
        print("\nThis record was sucessfully edited. Returning to main menu....\n")       
    # if the user enters R for remove the following block of code will be executed 
    elif answer == "r":
         # call the show vehicles function that will show all the vehicles in the database
        showVehicles(car_db)
        # prompt the user for the record number they would like to remove
        while True: 
            record_number = input("Please enter the record number you wish to remove: ")
            result = car_db.executeSelectQuery("SELECT * FROM vehicle_info")
            record_ok = False
            # declare for loop. For every record in result. If the record_number matches the user input, then record_ok equals true 
            for record in result:
                if record["record_number"] == record_number:
                    record_ok = True
                    break
            # if record_ok equals true we will break out of the loop. otherwise we will say that the record was not properly formatted.
            if record_ok == True:
                break
            else:
                print("Record number was not properly formatted or doesnt exist. Please try again. ")    
        # while loop that will continue until the user enters Y for yes to remove the record or N to keep the record on file 
        while True:
            # prompt user for input. If the user enters anything other than Y or N we will prompt them for it again. 
            # otherwise we will break out of the loop or if the user enters Y we will remove the record from the database and then break
            removeConfirm = input(f"Are you sure you want to remove record {record_number}? This action can only be undone by contacting the database administrator. Enter Y to remove or N to keep the record  ").lower()
            if removeConfirm == "y":
                car_db.executeQuery(f"UPDATE vehicle_info SET Deleted='YES' WHERE record_number='{record_number}'")
                car_db.conn.commit()
                print("This record was sucessfully deleted. Returning to main menu......")
                break
            elif removeConfirm == "n":
                print("This record will be kept on file. Returning to main menu......")
                break
            else:
                print("Please enter Y to remove or N to keep the record on file.")
    # if the user enters Q we will say goodbye and then break out of the loop 
    elif answer == "q":
        print("Goodbye! Have a great day!")
        break
    # if the user enters anything else, we will say their selection was invalid. Then we will prompt them for it again. 
    else:
        print("You entered an invalid selection. Please try again \n")




