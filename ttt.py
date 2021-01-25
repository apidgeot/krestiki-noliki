def cells():
    global field
    o = 0
    x = 0
    i = 0
    j = 0
    p = 0

    for _ in field:
        j = 0
        for _ in field[i]:
            if field[i][j] == "O":
                o += 1
            if field[i][j] == "X":
                x += 1
            j += 1
        i += 1


    i = 0
    for _ in field:
        if field[i][0] == field[i][1] and field[i][2] == field[i][1] and (field[i][2] == "O" or field[i][2] == "X"):
            print(field[i][0] + " wins")
            break
        elif field[0][i] == field[1][i] and field[2][i] == field[1][i] and (field[2][i] == "O" or field[2][i] == "X"):
            print(field[0][i] + " wins")
            break
        elif field[0][0] == field[1][1] and field[1][1] == field[2][2] and (field[2][2] == "O" or field[2][2] == "X"):
            print(field[0][0] + " wins")
            break
        elif field[0][2] == field[1][1] and field[1][1] == field[2][0] and (field[0][2] == "O" or field[0][2] == "X"):
            print(field[2][0] + " wins")
            break
        elif x + o == 9:
            print("Draw")
            break
        elif i == 2:
            print("Game not finished")
            p = 1
            break
        i += 1
    return p

def coordinates_X():
    global field
    cords = input("Enter coordinates: ").split()
    try:
        x = int(cords[1]) - 1
        y = int(cords[0]) - 1
    except ValueError:
        print("You should enter numbers!")
        return 0
    if x < 0 or x > 2 or y < 0 or y > 2:
        print("Coordinates should be from 1 to 3!")
        return 0
    if field[y][x] == "O" or field[y][x] == "X":
        print("This cell is occupied! Choose another one!")
        return 0
    field[y][x] = "X"
    string = "".join(field[0]) + "".join(field[1]) + "".join(field[2])
    field = string
    field = [[field[0], field[1], field[2]], [field[3], field[4], field[5]], [field[6], field[7], field[8]]]
    print("---------")
    print("| " + field[0][0] + " " + field[0][1] + " " + field[0][2] + " |")
    print("| " + field[1][0] + " " + field[1][1] + " " + field[1][2] + " |")
    print("| " + field[2][0] + " " + field[2][1] + " " + field[2][2] + " |")
    print("---------")
    return 1    

def coordinates_O():
    global field
    cords = input("Enter coordinates: ").split()
    try:
        x = int(cords[1]) - 1
        y = int(cords[0]) - 1
    except ValueError:
        print("You should enter numbers!")
        return 0
    if x < 0 or x > 2 or y < 0 or y > 2:
        print("Coordinates should be from 1 to 3!")
        return 0
    if field[y][x] == "O" or field[y][x] == "X":
        print("This cell is occupied! Choose another one!")
        return 0
    field[y][x] = "O"
    string = "".join(field[0]) + "".join(field[1]) + "".join(field[2])
    field = string
    field = [[field[0], field[1], field[2]], [field[3], field[4], field[5]], [field[6], field[7], field[8]]]
    print("---------")
    print("| " + field[0][0] + " " + field[0][1] + " " + field[0][2] + " |")
    print("| " + field[1][0] + " " + field[1][1] + " " + field[1][2] + " |")
    print("| " + field[2][0] + " " + field[2][1] + " " + field[2][2] + " |")
    print("---------")
    return 1
    

c = 0
field = "_________"
field = [[field[0], field[1], field[2]], [field[3], field[4], field[5]], [field[6], field[7], field[8]]]
print("---------")    
print("| " + field[0][0] + " " + field[0][1] + " " + field[0][2] + " |")
print("| " + field[1][0] + " " + field[1][1] + " " + field[1][2] + " |")
print("| " + field[2][0] + " " + field[2][1] + " " + field[2][2] + " |")
print("---------")
p = cells()
while p == 1:
    c = coordinates_X()
    p = cells()
    c = coordinates_O()
    p = cells()
