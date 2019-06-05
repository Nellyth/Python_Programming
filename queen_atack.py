try:
    file = open('data.txt')
except FileNotFoundError:
    print('The file does not exists')
    exit()

var = []
count = 0
for line in file.readlines():
    line = line.replace("\n", "")
    var.append(line.split(' '))
if var[0][1].isnumeric():
    if len(var) != int(var[0][1]) + 2:
        print('The file does not have the necessary lines')
        exit()
else:
    print('Only Accept numeric data')
    exit()
enter = 0
for i in var:
    if len(i) != 2:
        print('The lines have to contain two data, separated by a space')
        exit()
    if not i[0].isnumeric() or not i[1].isnumeric():
        print('All data must be numeric')
        exit()
    if int(i[0]) > int(var[0][0]) or int(i[0]) < 1 or int(i[1]) > int(var[0][0]) or int(i[1]) < 1:
        print('The data can not be less than 1 or the maximum number of the assigned table')
        exit()
    if enter > 1:
        if var[1][0] == i[0] and var[1][1] == i[1]:
            print('The position of the queen can not be repeated')
            exit()
    enter += 1

table = []
for i in range(int(var[0][0])):
    table.append([0] * int(var[0][0]))

if int(var[0][1]) != 0:
    for i in range(2, int(var[0][1]) + 2):
        table[int(var[i][0]) - 1][int(var[i][1]) - 1] = 'X'
table[int(var[1][0]) - 1][int(var[1][1]) - 1] = 'R'


def moves(row, column):
    max = int(var[0][0]) - 1
    if (row - 1 >= 0 and column - 1 >= 0):
        if (table[row - 1][column - 1] == 0):
            count_moves(row, column, -1, -1, max)

    if (column - 1 >= 0):
        if (table[row][column - 1] == 0):
            count_moves(row, column, 0, -1, max)

    if (row + 1 <= max and column - 1 >= 0):
        if (table[row + 1][column - 1] == 0):
            count_moves(row, column, 1, -1, max)

    if (row - 1 >= 0):
        if (table[row - 1][column] == 0):
            count_moves(row, column, -1, 0, max)

    if (row + 1 <= max):
        if (table[row + 1][column] == 0):
            count_moves(row, column, 1, 0, max)

    if (row - 1 >= 0 and column + 1 <= max):
        if (table[row - 1][column + 1] == 0):
            count_moves(row, column, -1, 1, max)

    if (column + 1 <= max):
        if (table[row][column + 1] == 0):
            count_moves(row, column, 0, 1, max)

    if (row + 1 <= max and column + 1 <= max):
        if (table[row + 1][column + 1] == 0):
            count_moves(row, column, 1, 1, max)


def count_moves(row, column, row_x, column_x, max):
    global count
    while True:
        if row_x == 1:
            row += 1
        if column_x == 1:
            column += 1
        if row_x == -1:
            row -= 1
        if column_x == -1:
            column -= 1

        if row > max or column > max or row < 0 or column < 0:
            return
        elif table[row][column] == 0:
            count += 1
        else:
            return


moves(int(var[1][0]) - 1, int(var[1][1]) - 1)
print(count)
for i in range(int(var[0][0])):
    print("")
    for j in range(int(var[0][0])):
        print("|", end="")
        middle = (5 - len(str(table[i][j]))) // 2
        for k in range(middle):
            print(" ", end="")
        print(table[i][j], end=" ")
        for k in range(middle):
            print(" ", end="")
        if ((5 - len(str(table[i][j]))) % 2 != 0):
            print(" ", end="")
    print("|", end="")
