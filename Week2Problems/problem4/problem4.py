# problem 4
import json

    
try:
    with open("text_files/my_car.json") as car_json:
        data = json.load(car_json)
        print("Your current car model is a " + data)
        
    
    answer = input("would you like to change your current car model? Enter Y or N ").lower()
    # while loop until the user is satisifed with their car model
    while answer != "n":
        with open("text_files/my_car.json", "w") as car_json:
            car = input("Enter the model of the car you drive: ")
            json.dump(car, car_json)
            answer = input("would you like to change your current car model? Enter Y or N ").lower()
# if the file my_car.json is not found then this code block will execute
except FileNotFoundError:
    answer = "y"
    # while loop until the user is satisifed with their car model
    while answer != "n":
        with open("text_files/my_car.json", "w") as car_json:
            car = input("Enter the model of the car you drive: ")
            json.dump(car, car_json)
        print("Your current car model is a " + car)
        answer = input("would you like to change your current car model? Enter Y or N ").lower()


 