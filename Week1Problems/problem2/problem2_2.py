from Functions.my_function import getWorkplace

workplaces = []

while True:
    workplace = getWorkplace()
    if workplace == "q":
        break
    else:
        workplaces.append(workplace)
print(f"Here are all the places you worked at: {workplaces}")

