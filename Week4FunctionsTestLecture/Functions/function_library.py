def getFirstName():
    """Get a user's first name from an input prompt"""

    ret_first_name = input("Please enter your first name: ")

    first_name_ok = False

    while not first_name_ok:
        first_name_ok = validate_name_part(ret_first_name)

        if not first_name_ok:
            ret_first_name = input("First name was not valid. Please try again: ")
            first_name_ok = validate_name_part(ret_first_name)
    
    return ret_first_name
