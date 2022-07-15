# declare the person class
class Person():
    """This class will be extended into the student and instructor classes"""
    def __init__(self, name, emailAddress, personID):
        """Intializes the attrbiute of the person class"""
        self.name = name
        self.emailAddress = emailAddress
        self.personID = personID