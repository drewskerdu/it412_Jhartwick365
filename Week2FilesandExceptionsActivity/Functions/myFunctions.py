import json
import os.path
import shutil
import time
def displayDictionary(dictionary):
    """This function will display a dictionary formatted Ill"""
    for key,value in dictionary.items():
        print(key + " - " + value)
    # print out a new line between the formatted values and the dicionary. 
    print()
   
def saveData(current_config):
    """This function is called if the user chooses to save their data."""
    if os.path.isfile("text_files/config_override.json"):
        shutil.copy2("text_files/config_override.json", "text_files/config_override.json.backup" + str(time.time()))
    #opening the config_override json file in write mode 
    with open("text_files/config_override.json", "w") as configOverride:
        json.dump(current_config, configOverride)


def loadDataFromUserConfig(current_config):
    """This function opens user data from the proper configuration file"""
    # if the file config_override exists, I would load the data from there.  If it doesn't I will load data from basic config
    # Then I will return the current configuration back into our main program  
    try:
        with open("text_files/config_override.json") as configOverride:
            current_config = json.load(configOverride)
        return current_config 
    except FileNotFoundError:
        with open("text_files/basic_config.json") as basicConfig:
            current_config = json.load(basicConfig)
        return current_config


def modifyAttribute(current_config):
    """This function is called if the user chooses to modify a attribute """
    # declare while loop 
    while True:
        # call the display current config function that will display the current configuration
        displayDictionary(current_config)
        modify_attribute = input("\nWhich of these attributes would you like to modify? ")
        # if the modifed attribute is in the current configuration, I would prompt the user to see what they want to set it to. 
        if modify_attribute in current_config:
            attribute_modification = input("\nWhat would you like to set " + modify_attribute + " to? ")
            # adding the attribute to current config
            current_config[modify_attribute] = attribute_modification
            print("\n" + modify_attribute + " will be set to " + attribute_modification + " if you choose to save your changes later\n")
            break
        # if the attribute is not in current_config I would say that the attribute was not formatted correctly, it would prompt the user again to enter it. 
        else:
            print("\nAttribute was not formatted correctly. Please try again")
    return current_config

def addAttribute(current_config, optional_attributes):
    """This function will be called if the user chooses to add an attribute"""
    # declare while loop 
    while True:
        # prompt the user to see which attribute they would like to add
        displayDictionary(optional_attributes)

        add_attribute = input("\nWhich of these attributes would you like to add to the configuration? ")
        # declare for loop control variable 
        found = False
        # for loop that will search for the attribute entered. If it is found, I will add the attribute to current config
        for attribute , value in optional_attributes.items():
            if add_attribute == attribute:
                found = True
                current_config[attribute] = value
                break

        # if found is still False I would say that the attribute was not formatted correctly.      
        if found == False:
            print("Attribute was not formatted correctly. Please try again. ")
        else:
            # remove the attribute from optional attributes so the user will not be given the option to add it again
            del optional_attributes[add_attribute]
            print("\n" + add_attribute + " will be added to the configuration if you choose to save your changes later. \n")
            break
    return current_config, optional_attributes

def removeAttribute(optional_attributes, current_config):
    """This function will be called if the user chooses to remove an attribute"""
    # declare attributes that are optional dictionary. The second dictionary will not change. 
    removalAttributes = {"Allow File Uploads" : "Yes", "Use Caching" : "Yes", "Caching File" : "cache/filecache.cache", "Mail Host" : "mail.apphost.com"}
    attributes_optional = {"Allow File Uploads" : "Yes", "Use Caching" : "Yes", "Caching File" : "cache/filecache.cache", "Mail Host" : "mail.apphost.com"}
    # remove optional attributes that are not in current config
    for key, value in attributes_optional.items():
        if key not in current_config:
            del removalAttributes[key]
    # declare basic config keys list
    basic_config_keys = ["Safe Mode", "Memory", "Error Log"]

    # declare outer while loop 
    while True:
        # Prompt the user for which attribute they would like to remove
        displayDictionary(removalAttributes)
        remove_attribute = input("Which of these attributes would you like to remove from the configuration? ")
        # if the attribute is any of the basic attributes I will say that it is required
        if remove_attribute in basic_config_keys:
            print("\nYou cannot remove this attribute because it is required. Please try again ")
        # If the attribute is in current config, I will use a for loop to find the value that is in current_config 
        elif remove_attribute in current_config:
            for attribute , value in removalAttributes.items():
                # if the attribute matches the removed attribute entered I will remove it from the current configuration
                if attribute == remove_attribute:
                    del current_config[attribute]
                    optional_attributes[attribute] = value
                    print("\n" + remove_attribute + " will be removed from the configuration if you choose to save your changes later.\n ")
            break
        # if the attribute was not in current_config or basic_config, I will say that the attribute was not properly formated 
        else:
            print("Attribute was not formatted correctly. Please try again. ")  
    return current_config, optional_attributes

    