# declare the Validator class that will use different methods to validate submitted information 
class Validator():
    def __init__(self):
        """This constructor is empty because there are no real attrbiutes this class has"""
    
    def validateEmail(self, email):
        """This method validates the email inputted by the user"""
        badCharacters = ["!", '"', "'", "#", "$", "%", "^", "&", "*", "(", ")", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", '"\"', ")"]
        hasBadCharacters = False
        # for loop to determine if there are any bad characters in the name
        for character in badCharacters:
            if character in email:
                hasBadCharacters = True
                break
        # if the hasBadCharacters variable comes back as true we will return false, otherwise it will return true
        if hasBadCharacters == True or len(email) == 0:
            return False
        else:
            return True
    def validatePersonID(self, personID, maxLength):
        """This method validates the instructorID inputted by the user"""
        # if the instructorID has anything other than digits in it or if it is more than 5 digits we would return false. Otherwise it will return true
        digitTest = personID.isdigit()
        if digitTest == False or len(personID) > maxLength:
            return False
        else:
            return True

    def validateName(self, name):
        """This method validates the name inputed by the user"""
        badCharacters = ["!", '"', "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}"]
        hasBadCharacters = False
        # for loop to determine if there are any bad characters in the name
        for character in badCharacters:
            if character in name:
                hasBadCharacters = True
                break
        # if the hasBadCharacters variable comes back as true we will return false, otherwise it will return true
        if hasBadCharacters == True or len(name) == 0:
            return False
        else:
            return True