class Clothing():
    """This class is  a base class for different articles of clothing """
    def __init__(self, size, color, quantity=1):
        """This constructor intalizes the different clothing attributes"""
        self.size = size
        self.color = color
        self.quantity = quantity
    def decreaseQuantity(self, value):
        """This methods decreases the quantity attribute with a specified value"""
        self.quantity = self.quantity - value
    def increaseQuantity(self, value):
        """This method decreases the quantity attribute with a specifed value  """
        self.quantity = self.quantity + value