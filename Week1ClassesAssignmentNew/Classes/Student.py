from Classes.Person import Person
class Student(Person):
    """This class stores the student records"""
    def __init__(self, name, emailAddress, studentID, programStudy):
        """This constructor intializes the student attributes"""
        super().__init__(name, emailAddress, studentID)
        self.programStudy = programStudy
    def displayInformation(self):
        """This method displays the students attributes"""
        print(f"{self.name.title()}'s id number is {self.personID}, his program of study is {self.programStudy}, and his email address is {self.emailAddress}")