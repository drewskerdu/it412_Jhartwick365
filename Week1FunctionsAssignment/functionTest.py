from Functions.my_functions import divideTwoNumbers
from Functions.my_functions import multiplyTwoNumbers

division_list = [{"top_number": "1", "bottom_number": 2}, {"top_number": 5, "bottom_number": 8}]
the_result = divideTwoNumbers(division_list)
print("The result of division is ")
print(the_result)

multiply_list = [{"top_number": "1", "bottom_number": 2}, {"top_number": 5, "bottom_number": 8}]
the_result = multiplyTwoNumbers(multiply_list)
print("The result of multiplication is ")
print(the_result)