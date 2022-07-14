from Classes.Clothing import Clothing
class ShirtInherit(Clothing):
    def __init__(self, size, color, quantity, type, message):
        """Intalizes the ShirtInherit's attributes"""
        super().__init__(size, color, quantity)
        self.type = type
        self.message = message
    def printMessage(self):
        """Prints the message on the shirt"""
        print("The message on the shirt is: '" + self.message + "'")
