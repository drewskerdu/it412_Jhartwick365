from Classes.Clothing import Clothing
from Classes.ShirtInherit import ShirtInherit

graphic_shirt = ShirtInherit("Extra Large", "Green", 5, "Long-Sleeve", "Warning: may talk about roller coasters at any time")
graphic_shirt.increaseQuantity(5)
print(graphic_shirt.quantity)
graphic_shirt.printMessage()