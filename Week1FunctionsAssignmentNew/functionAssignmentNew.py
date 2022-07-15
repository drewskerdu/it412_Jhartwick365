from Functions.my_functions import *
#set increment count variable to 0
count = 0
while count < 5:
    # control variable for the employee id loop
    # get and validate employee id from user by calling that function 
    employeeId = getEmployeeId()
    
    # get and validate employee name from user by calling that function 
    employeeName = getEmployeeName()
    
    # get employee email address from user by calling that function
    employeeEmailAddress = getEmployeeEmail()
    
    # get employees home address from user 
    employeeAddress = getEmployeeAddress()
    
    employeeData = []
    # append employee data into the dictionary
    # if an employee address is not provided or invalid the first if statement will be executed If an address is provided the else statement will be executed
    if len(employeeAddress) == 0: 
        employeeData = appendEntryToDictionaryList(employeeData, employeeId, employeeName, employeeEmailAddress)
    else: 
       employeeData = appendEntryToDictionaryList(employeeData, employeeId, employeeName, employeeEmailAddress, employeeAddress)

    # prompt the user if they want to enter another employee
    # if they type N we break the loop and print the dictionairy
    # if they type Y it would prompt them for another users input 
    if count <= 4: 
        enterAnotherEmployee = input("Would you like to enter data for another employee (type Y or N)? ").lower()
    else:
        print("You can only enter data for 5 employees at a time. Goodbye!")
        break
    
    if enterAnotherEmployee == "n":
        break
    elif enterAnotherEmployee == "y":
        count += 1
# print out the employee data dictionary
print("Here are the employee(s) that were entered into our database: ")
print(employeeData)