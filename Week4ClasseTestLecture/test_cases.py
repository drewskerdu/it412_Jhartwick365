from Classes.pizza import Pizza

pizza_done = False

my_pizza = Pizza("Mike's Pizza")

while not pizza_done:
    done_answer = input("Are you done with your pizza(Y or N)? ")
    if done_answer.lower() == "n":
        pizza_action = input("Do you want to add or remove a pizza topping (A/R)? ")
        if pizza_action.lower() == "a":
            pizza_topping = input("Please tell me what you'd like on the pizza: ")
            my_pizza.addTopping(pizza_topping)
        else:
            pizza_topping = input("Please tell me what you would like to remove from the pizza: ")
            my_pizza.removeTopping(pizza_topping)
    else:
        pizza_done = True

print("Here are the topping on the pizza: ")
print(my_pizza.toppings)