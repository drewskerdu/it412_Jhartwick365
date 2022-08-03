# create task method
class Task():
    # declare constructor
    def __init__(self, name, description, time):
        """This intalizes my attributes of my task class"""
        self.name = name
        self.description = description
        self.time = time
    def increase_time(self):
        """This method increases the time attribute by 1"""
        self.time = self.time + 1
    def decrease_time(self):
        """This method decreass the time attribute by 1"""
        self.time = self.time - 1
    def reset_time(self):
        """This method resets the time attribute to 0"""
        self.time = 0