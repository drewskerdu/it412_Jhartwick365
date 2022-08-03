from Classes.Task import Task
import unittest
# declare task test class 
class Task_test(unittest.TestCase):
    # create an instance of a task for doing dishes
    def setUp(self):
        self.dishes = Task("Dishes", "Wash dishes in sink", 15)
    # test increase time method
    def testIncreaseTime1(self):
        self.dishes.increase_time()
        self.assertEqual(self.dishes.time, 16)
        self.dishes.increase_time()
        self.assertEqual(self.dishes.time, 17)
    # test decrease time method
    def testDecreaseTime(self):
        self.dishes.decrease_time()
        self.assertEqual(self.dishes.time, 14)
        self.dishes.decrease_time()
        self.assertEqual(self.dishes.time, 13)
    # test reset time method
    def testResetTime(self):
        self.dishes.reset_time()
        self.assertEqual(self.dishes.time, 0)
        
