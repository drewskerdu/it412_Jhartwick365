import Functions.my_function as JobsFunction



workplaces = []

while True:
    workplace = JobsFunction.getWorkplace()
    if workplace == "q":
        break
    else:
        workplaces.append(workplace)
print(f"Here are all the places you worked at: {workplaces}")


