from Classes.pet import Pet

class Cat(Pet):
    """A simple class for representing a cat"""
    def __init__(self, name, age):
        """Initialize name and age variables/attributes for the cat"""
        super().__init__(name, age)