n = int(input())
matrix = []
arrows = []
sub_row = 0
sub_column = 0
destroyed = False
health = 3
cruisers = 3

for x in range(n):
    bebob = [y for y in input()]
    matrix.append(bebob)
    bebob = []

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if matrix[row][column] == 'S':
            sub_row = row
            sub_column = column

while not destroyed:
    command = input()
    if command == "up":
        matrix[sub_row][sub_column] = "-"
        sub_row -= 1
        if matrix[sub_row][sub_column] == "*":
            health -= 1
            matrix[sub_row][sub_column] = "S"
        elif matrix[sub_row][sub_column] == "C":
            cruisers -= 1
            matrix[sub_row][sub_column] = "S"
        else:
            matrix[sub_row][sub_column] = "S"
    if command == "down":
        matrix[sub_row][sub_column] = "-"
        sub_row += 1
        if matrix[sub_row][sub_column] == "*":
            health -= 1
            matrix[sub_row][sub_column] = "S"
        elif matrix[sub_row][sub_column] == "C":
            cruisers -= 1
            matrix[sub_row][sub_column] = "S"
        else:
            matrix[sub_row][sub_column] = "S"
    if command == "left":
        matrix[sub_row][sub_column] = "-"
        sub_column -= 1
        if matrix[sub_row][sub_column] == "*":
            health -= 1
            matrix[sub_row][sub_column] = "S"
        elif matrix[sub_row][sub_column] == "C":
            cruisers -= 1
            matrix[sub_row][sub_column] = "S"
        else:
            matrix[sub_row][sub_column] = "S"
    if command == "right":
        matrix[sub_row][sub_column] = "-"
        sub_column += 1
        if matrix[sub_row][sub_column] == "*":
            health -= 1
            matrix[sub_row][sub_column] = "S"
        elif matrix[sub_row][sub_column] == "C":
            cruisers -= 1
            matrix[sub_row][sub_column] = "S"
        else:
            matrix[sub_row][sub_column] = "S"
    if health == 0:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{sub_row}, {sub_column}]!")
        for z in matrix:
            print(''.join(z))
        destroyed = True
    if cruisers == 0:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        for z in matrix:
            print(''.join(z))
        break
    #for z in matrix:
        #print(''.join(z))
    #print("NEXT")
