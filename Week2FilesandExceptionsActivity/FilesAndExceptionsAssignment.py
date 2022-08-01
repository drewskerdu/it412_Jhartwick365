# import myFunctions into my program 
from Functions.myFunctions import *
# declare configuration data list that will store the current configuration. 
current_config = {}
# declare optional attributes list. Stores attributes that are currenly optional. 
# Note: attribute will be removed if the user already has it in their configuration
optional_attributes = {"Allow File Uploads" : "Yes", "Use Caching" : "Yes", "Caching File" : "cache/filecache.cache", "Mail Host" : "mail.apphost.com"}

# call current config function that will load the current configuration 
current_config = loadDataFromUserConfig(current_config)

# declare attributes delete dictionary that will store the attribute that are already configured in current config. 
attributes_del = {}

# for loop that will get attributes from optional attributes that appear in current config and store them in attributes del
for key in optional_attributes.keys():
    if key in current_config:
        attributes_del[key] = optional_attributes[key]

# for every attributs in attributed_del it will delete them from optional attributes. Therefore, the user will not be given the option to add them again 
for key in attributes_del.keys():
    del optional_attributes[key]

#declare while loop control variable
answer = "k"
# declare outer while loop that will go until the user enters Q to quit
while answer != "q":
    # get information from user.
    print("Here is the current configuration: ")
    displayDictionary(current_config)
    answer = input("Would you like to modify, add, or remove a attribute?\nEnter M for modify, A for add, R for remove, or q to quit: ").lower()
    # if the user enters m, I will call our modify attribute function 
    if answer == "m":
        current_config = modifyAttribute(current_config)
    # if the user enters a, I will call our add attribute function
    elif answer == "a":
        current_config, optional_attributes = addAttribute(current_config, optional_attributes)
    # if the user enters r, I will call our remove attributes function
    elif answer == "r":
        current_config, optional_attributes = removeAttribute(optional_attributes, current_config)
    # if the user anything else, I will prompt the user again for their information. 
    else:
        print("Answer was not properly formatted. Please try again. ")
# end while loop
# if the length of the system_modification dictionary doesn't equal 0, I will prompt the user to save their changes. Otherwise I will end the program. 

while True: 
    # prompt the user to save changes   
    saveChanges = input("\nWould you like to save your changes enter y or n? ").lower()
    # if the user enters Y, I would call our saveData function.
    if saveChanges == "y":
        saveData(current_config)
        print("Your changes have been saved. Have a great day!")
        break
    # if the user enters N, I would end the program.
    elif answer == "n":
        print("Goodbye! Have a great day!")
        break
    # if the user enters anything else, I will prompt them to enter it again. 
    else:
        print("Please enter Y for yes or N for no. ")


            
        


            





