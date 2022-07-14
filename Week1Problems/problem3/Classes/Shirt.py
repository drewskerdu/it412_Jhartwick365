class Shirt():
    """Creates a basic shirt class"""
    def __init__(self, size, color):
        """Intalizes the shirts attributes"""
        self.size = size
        self.color = color
    
    def printSizeandColor(self):
        """This method prints out the size and color attributes"""
        print("The size of this shirt is a " + self.size)
        print("The color of this shirt is " + self.color)