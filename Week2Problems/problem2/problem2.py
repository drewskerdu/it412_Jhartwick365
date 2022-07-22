


with open("text_files/dinner_menu.txt","w") as menu:
    dinner = "l"
    while dinner != "q":
        dinner = input("What would you like for dinner next week? Or enter Q to quit: ")
        if dinner != "q":
            menu.write(dinner + "\n")
