
with open("text_files/SacramentocrimeJanuary2006.csv") as csv_file:
    for line in csv_file:
        temp_line = line.split(",")
        place_counter = 0 
        while place_counter < len(temp_line):
            temp_line[place_counter] = temp_line[place_counter][1:-1]
            if place_counter == 0:
                print(temp_line[place_counter])
            if place_counter == 1:
                print(temp_line[place_counter])
            if place_counter == 5:
                print(temp_line[place_counter] + "\n\n")
            place_counter = place_counter + 1
        