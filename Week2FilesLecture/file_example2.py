import os.path
import shutil
import time

temp_output = ""


with open("text_files/pet.py") as python_file:
    for line in python_file:
        temp_line = line.strip()
        if temp_line.startswith("#") or temp_line.startswith('"""'):
            pass
        else:
            temp_output = temp_output + line

if os.path.isfile("text_files/cleaned_output.py"):
    shutil.copy2("text_files/cleaned_output.py", "text_files/cleaned_output.py.backup" + str(time.time()))

with open("text_files/cleaned_output.py", "w") as file_output:
    file_output.write(temp_output)
