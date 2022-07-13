from Classes.pet import Pet
class Dog(Pet):
    """A simple class for representing a dog"""

    def __init__(self, name, age, breed):
        """Initialize name and age variables/attributes for the dog"""
        super().__init__(name, age)
        self.breed =  breed

    def placeDoginCarrier(self):
        """This represents placing the dog in a car carrier"""
        print(self.name + " is in the dog carrier!")

    def takeToVet(self):
        """Contains all of the tasks needed to get the dog to the vet"""
        self.placeDoginCarrier()
        self.__visitVet()
    
    def __visitVet(self):
        """Represents the act of taking the dog to the vet"""
        print(self.name + " is on their way to the vet!")