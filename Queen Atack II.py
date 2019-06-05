try:
    archivo = open('Data.txt')
except FileNotFoundError:
    print('El Archivo es Incorrecto')
    exit()

var = []
count = 0
for linea in archivo.readlines():
    linea = linea.replace("\n","")
    var.append(linea.split(' '))
if var[0][1].isnumeric():
    if len(var) != int(var[0][1])+2:
        print('El Archivo es Incorrecto')
        exit()
else:
    print('El Archivo es Incorrecto')
    exit()
enter=0
for i in var:
    if len(i) != 2:
        print('El Archivo es Incorrecto')
        exit()
    if not i[0].isnumeric() or not i[1].isnumeric():
        print('El Archivo es Incorrecto')
        exit()
    if int(i[0]) > int(var[0][0]) or int(i[0]) < 1 or int(i[1]) > int(var[0][0]) or int(i[1]) < 1:
        print('El Archivo es Incorrecto')
        exit()
    if enter>1:
        if var[1][0] == i[0] and var[1][1] == i[1]:
            print('El Archivo es Incorrecto')
            exit()
    enter += 1

tablero = []
for i in range(int(var[0][0])):
    tablero.append([0]*int(var[0][0]))

if int(var[0][1]) != 0:
    for i in range(2, int(var[0][1])+2):
        tablero[int(var[i][0])-1][int(var[i][1])-1]='X'
tablero[int(var[1][0])-1][int(var[1][1])-1] = 'R'


def movimientos(fila,column):
    max = int(var[0][0])-1
    if (fila - 1 >= 0 and column - 1 >= 0):
        if (tablero[fila - 1][column - 1] == 0):
            conteo(fila, column, -1, -1, max)

    if (column - 1 >= 0):
        if (tablero[fila][column - 1] == 0):
            conteo(fila, column, 0, -1, max)

    if (fila + 1 <= max and column - 1 >= 0):
        if (tablero[fila + 1][column - 1] == 0):
            conteo(fila, column, 1, -1, max)

    if (fila - 1 >= 0):
        if (tablero[fila - 1][column] == 0):
            conteo(fila, column, -1, 0, max)

    if (fila + 1 <= max):
        if (tablero[fila + 1][column] == 0):
            conteo(fila, column, 1, 0, max)

    if (fila - 1 >= 0 and column + 1 <= max):
        if (tablero[fila - 1][column + 1] == 0):
            conteo(fila, column, -1, 1, max)

    if (column + 1 <= max):
        if (tablero[fila][column + 1] == 0):
            conteo(fila, column, 0, 1, max)

    if (fila + 1 <= max and column + 1 <= max):
        if (tablero[fila + 1][column + 1] == 0):
            conteo(fila, column, 1, 1, max)


def conteo(fila, column, filax, columnx, max):
    global count
    while True:
        if filax == 1:
            fila+=1
        if columnx == 1:
            column+=1
        if filax == -1:
            fila -= 1
        if columnx == -1:
            column-=1

        if fila>max or column > max or fila<0 or column<0:
            return
        elif tablero[fila][column]==0:
            count+=1
        else:
            return


movimientos(int(var[1][0])-1,int(var[1][1])-1)
print(count)
for i in range(int(var[0][0])):
    print("")
    for j in range(int(var[0][0])):
        print("|",end="")
        mitad = (5 - len(str(tablero[i][j]))) // 2
        for k in range(mitad):
            print(" ",end="")
        print(tablero[i][j],end=" ")
        for k in range(mitad):
            print(" ",end="")
        if((5-len(str(tablero[i][j])))%2!=0):
            print(" ",end="")
    print("|", end="")
