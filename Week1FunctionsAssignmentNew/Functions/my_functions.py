# declare get employee id function that will return an emplyoee id
def getEmployeeId():
    employeeIdCheck = False
    while employeeIdCheck == False:
        # prompt the user for their employee id
        employeeId = input("Please enter a employee id: ")
        # call employee id checker function 
        employeeIdChecker = checkEmployeeId(employeeId)
        # if the employee id was not formatted correctly we prompt the user again. otherwise we continue 
        if employeeIdChecker == False:
            print("Employee id was not formatted correctly. Please try again. ")
        else:
            employeeIdCheck = True
    return employeeId
# declare get employee name function that will return the employees name
def getEmployeeName():
    # employee name while loop control variable
    employeeNameCheck = False
    while employeeNameCheck == False:
        employeeName = input("Please enter a first name: ")
        # check employee name for anything other than letters 
        employeeNameChecker = checkEmployeeName(employeeName)
        #  if the employee name was not formatted correctly we prompt the user again. otherwise we continue 
        if employeeNameChecker == False:
            print("Employee name was not properly formatted. Please try again. ")
        else:
            employeeNameCheck = True
    return employeeName
# declare get employee email function that will return the employees email
def getEmployeeEmail():
    # declare email address control variable     
    employeeEmailAddressCheck = False
    while employeeEmailAddressCheck == False:
        employeeEmailAddress = input("Please enter an email address: ")
        # validate employee email address using that function 
        employeeEmailChecker = checkEmployeeEmail(employeeEmailAddress)
        #if the check employee email function comes back as false we reprompt the user otherwise it continues 
        if employeeEmailChecker == False:
            print("Employee email was not properly formatted. Please try again. ")
        else:
            employeeEmailAddressCheck = True
    return employeeEmailAddress
# declare get employee address function that will return the employees address
def getEmployeeAddress():
    # declare home address control variable 
    employeeAddressCheck = False
    while employeeAddressCheck == False:
        employeeAddress = input("Please enter the employee's home address(optional): ")
        # call employee address checker function
        employeeAddressChecker = checkEmployeeAddress(employeeAddress)
        # test to see if bad characters came up in the for loop for address. If so we reprompt the user, otherwise we continue
        if employeeAddressChecker == False:
            print("Address was not properly formatted. Please try again. ")
        else:
            employeeAddressCheck = True
    return employeeAddress
# declare check employee id function that will validate employee ids
def checkEmployeeId(employeeId):
    # check employee id to see if it is a digit or greater than 7 digits
    employeeIdCheck = employeeId.isdigit()
    if len(employeeId) >= 8 or employeeIdCheck == False:
        return False
    else:
        return True
    
# declare check employee name function that will check the employee name for bad characters
def checkEmployeeName(name):
    # declare bad characters list for name
    nameBadChars = ['!', '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+' ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}',')']        
    numbersCheck = name.isalpha()
    # for loop to test if any unwanted characters are in the employees name. if they are we return false otherwise we return true
    hasBadCharacters = False
    for character in nameBadChars:
        if character in name:
            hasBadCharacters = True
    if hasBadCharacters == True or len(name) == 0 or numbersCheck == False:
        return False 
    else: 
        return True
# check employee email function that will check the employees email for formatting
def checkEmployeeEmail(email):
    emailBadChars = ['!', '"', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+' ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}',')']
    hasBadCharacters = False
   # for loop to test if any unwanted characters are in the employees name. if they are we return false otherwise we return true
    for character in emailBadChars:
        if character in email:
            hasBadCharacters = True
    if hasBadCharacters == True or len(email) == 0:
        return False
    else:
        return True
#declare check employee address function that will check employee addresses
def checkEmployeeAddress(address):
    addressBadChars = ['!', '"', "'", '@', '$', '%', '^', '&', '*', '_', '=', '+', '<', '>',  '?', ';', ':', '[', ']', '{', '}', ')']
    # for loop to test if any unwanted characters are in the employees name. if they are we return false otherwise we return true
    hasBadCharacters = False
    for charactor in addressBadChars:
        if charactor in address:
            hasBadCharacters = True
            break
    if hasBadCharacters == True:
        return False
    else: 
        return True
#declare append entry to dictionary function that will append the data to the dictionary 
def appendEntryToDictionaryList(employeeData, employeeId, employeeName, employeeEmail, employeeAddress=''):
    if employeeAddress == '':
        employeeData.append({"EmployeeId": employeeId,"Name": employeeName.title(),"EmailAddress": employeeEmail})
    else:
        employeeData.append({"EmployeeId": employeeId,"Name": employeeName.title(),"EmailAddress": employeeEmail,"HomeAddress": employeeAddress})
    return employeeData