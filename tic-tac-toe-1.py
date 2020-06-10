# Stage 3/5
"""
a = input("Enter cells:")

# create field as an empty list and fill it with other 3 empty lists:
field = []
list_ = [field.append([]) for x in range(3)]

# fill the field with the input chars:
for x in range(3):
    for y in range(3):
        field[x].append(a[x * 3 + y])

# print the filled field:
print("-" * 9)
for x in range(3):
    print(f"| {field[x][0]} {field[x][1]} {field[x][2]} |")
print("-" * 9)

win_x = ["X", "X", "X"]
win_o = ["O", "O", "O"]

# create the state of the field:
state = ""

# check if (count of X - count of O) is more than 1:
if abs(a.count("X") - a.count("O")) > 1:
    state = "Impossible"

# check if there are both 3 X in row and 3 O in row (both X and O won):
for x in range(3):
    for y in range(3):
        if x != y and field[x] == win_x and field[y] == win_o:
           state = "Impossible"
        elif x != y and field[0][x] == "X" and field[1][x] == "X" and field[2][x] == "X" and field[0][y] == "O" and field[1][y] == "O" and field[2][y] == "O":
            state = "Impossible"

# if state not impossible check if X or O wins:
if state != "Impossible":
    # check horizontals if X or O wins:
    for f in field:
        if f == win_x:
            state = "X wins"
        if f == win_o:
            state = "O wins"
    # check verticals if X or O wins:
    for x in range(3):
        for y in range(3):
            if x != y and field[0][x] == "X" and field[1][x] == "X" and field[2][x] == "X":
                state = "X wins"
            if x != y and field[0][y] == "O" and field[1][y] == "O" and field[2][y] == "O":
                state = "O wins"
    # check diagonals if X or O wins:
    if [field[x][x] for x in range(3)] == win_x or [field[x][2 - x] for x in range(3)] == win_x:
        state = "X wins"
    elif [field[x][x] for x in range(3)] == win_o or [field[x][2 - x] for x in range(3)] == win_o:
        state = "O wins"

# check if there are empty fields and game can continue or not:
if state not in ["Impossible", "X wins", "O wins"]:
    state = "Draw"
    for f in field:
        if "_" in f or " " in f:
            state = "Game not finished"

print(state)
"""

# Stage 4/5
# First move!

"""
# create field as an empty list and fill it with other 3 empty lists:
field = []
list_ = [field.append([]) for x in range(3)]

# create function fill_field that asks input and fills the field with input chars
def fill_field():
    a = input("Enter cells:")

    # fill the field with the input chars:
    for x in range(3):
        for y in range(3):
            field[x].append(a[x * 3 + y])

# create function print_field that prints the filled field:
def print_field():
    print("-" * 9)
    for x in range(3):
        print(f"| {field[x][0]} {field[x][1]} {field[x][2]} |")
    print("-" * 9)

fill_field()
print_field()

coordinates = 0

while coordinates == 0:
    # ask user field coordinates to place X
    a, b = input("Enter cells:").split()

    if a not in "0123456789" or b not in "0123456789":
        # if the users enter other symbols
        print("You should enter numbers!")

    elif int(a) not in range(1, 4) or int(b) not in range(1, 4):
        # if the coordinates are outside the field
        print("Coordinates should be from 1 to 3!")

    else:
        a = int(a) - 1
        b = 3 - int(b)

        if field[b][a] in ["X", "O"]:
            # if field not empty
            print("This cell is occupied! Choose another one!")

        elif field[b][a] in [" ", "_"]:
            # if the field is empty and the coordinates are valid -> fill the cell
            coordinates = 1
            field[b][a] = "X"
            print_field()
"""

# Stage 5/5
# Fight!

value = "X"
turn = "player_x"

win_x = ["X", "X", "X"]
win_o = ["O", "O", "O"]

# create the state of the field:
state = "Game not finished"

# create field as an empty list and fill it with other 3 empty lists:
field = []
list_ = [field.append([" ", " ", " "]) for x in range(3)]

# create function print_field() that prints the filled field:
def print_field():
    print("-" * 9)
    for x in range(3):
        print(f"| {field[x][0]} {field[x][1]} {field[x][2]} |")
    print("-" * 9)


#create function check_field() that checks the state of the field
def check_field():
    global state
    # check if (count of X - count of O) is more than 1:
    count_x = 0
    count_o = 0
    for x in range(3):
        for cell in field[x]:
            if cell == "X":
                count_x += 1
            if cell == "O":
                count_o += 1
    if abs(count_x - count_o) > 1:
        state = "Impossible1"

    # check if there are both 3 X in row and 3 O in row (both X and O won):
    for x in range(3):
        for y in range(3):
            if x != y and field[x] == win_x and field[y] == win_o:
                state = "Impossible2"
            elif x != y and field[0][x] == "X" and field[1][x] == "X" and field[2][x] == "X" and field[0][y] == "O" and field[1][y] == "O" and field[2][y] == "O":
                state = "Impossible3"

    # if state not impossible check if X or O wins:
    if state not in ["Impossible1", "Impossible2", "Impossible3"]:
        # check horizontals if X or O wins:
        for f in field:
            if f == win_x:
                state = "X wins"
            if f == win_o:
                state = "O wins"
        # check verticals if X or O wins:
        for x in range(3):
            for y in range(3):
                if x != y and field[0][x] == "X" and field[1][x] == "X" and field[2][x] == "X":
                    state = "X wins"
                if x != y and field[0][y] == "O" and field[1][y] == "O" and field[2][y] == "O":
                    state = "O wins"
        # check diagonals if X or O wins:
        if [field[x][x] for x in range(3)] == win_x or [field[x][2 - x] for x in range(3)] == win_x:
            state = "X wins"
        elif [field[x][x] for x in range(3)] == win_o or [field[x][2 - x] for x in range(3)] == win_o:
            state = "O wins"

    # check if there are empty fields and game can continue or not:
    if state not in ["Impossible", "X wins", "O wins"]:
        state = "Draw"
        for f in field:
            if "_" in f or " " in f:
                state = "Game not finished"


# create fuction change_player():
def change_player():
    global value
    if value == "X":
        value = "O"
    elif value == "O":
        value = "X"

print_field()
check_field()

while state not in ["X wins", "O wins", "Draw"]:
    # ask user field coordinates to place X
    a, b = input("Enter the coordinates:").strip().split()

    if a not in "0123456789" or b not in "0123456789":
        # if the users enter other symbols
        print("You should enter numbers!")

    elif int(a) not in range(1, 4) or int(b) not in range(1, 4):
        # if the coordinates are outside the field
        print("Coordinates should be from 1 to 3!")

    else:
        a = int(a) - 1
        b = 3 - int(b)

        if field[b][a] in ["X", "O"]:
            # if field not empty
            print("This cell is occupied! Choose another one!")

        elif field[b][a] in [" ", "_"]:
            # if the field is empty and the coordinates are valid -> place value
            field[b][a] = value
            print_field()
            change_player()
            check_field()

print(state)
