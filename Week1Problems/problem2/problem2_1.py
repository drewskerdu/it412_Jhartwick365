import Functions.my_function


workplaces = []

while True:
    workplace = Functions.my_function.getWorkplace()
    if workplace == "q":
        break
    else:
        workplaces.append(workplace)
print(f"Here are all the places you worked at: {workplaces}")

