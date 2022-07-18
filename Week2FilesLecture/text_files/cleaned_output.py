class Pet():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def clean(self):
        print(self.name + " is clean!")