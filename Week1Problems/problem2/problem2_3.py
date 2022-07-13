from Functions.my_function import getWorkplace as jobs

workplaces = []

while True:
    workplace = jobs()
    if workplace == "q":
        break
    else:
        workplaces.append(workplace)
print(f"Here are all the places you worked at: {workplaces}")


