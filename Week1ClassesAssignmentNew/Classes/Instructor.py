from Classes.Person import Person
# declare the instructor class that will store information about the instructor
class Instructor(Person):
    """This class stores the instructor records"""
    def __init__(self, name, emailAddress, instructorID, institution, highestDegree):
        """This constructor intializes the instructor attributes"""
        super().__init__(name, emailAddress, instructorID)
        self.institution = institution
        self.highestDegree = highestDegree
    def displayInformation(self):
        """This method displays the instructors attributes"""
        print(f"{self.name.title()}'s id number is {self.personID} and his email address is {self.emailAddress}.")
        print(f"The highest degree {self.name.title()} earned is {self.highestDegree} and the recent college attended was {self.institution}")