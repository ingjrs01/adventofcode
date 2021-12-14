def load():
    matrix = []
    lines = [ line.strip() for line in open('real','r').readlines()]

    for line in lines:
        row = []
        for i in range(len(line)):
            row.append(line[i])
        matrix.append(line)

    return matrix

def count_occupied(pos,matrix):
    total = 0
    x,y = pos
    if (x > 0): # Puedo mirar la fila superior
        if (y > 0):
            i = x
            j = y
            salir = False
            while not salir: 
                # Mirar toda la diagonal
                i -= 1
                j -= 1
                if (i >= 0 and j >= 0):
                    if (matrix[i][j]=="#"):
                        salir = True
                        total += 1
                    if (matrix[i][j]=="L"):
                        salir = True
                else:
                    salir = True
        # Diagonal derecha
        if (y < len(matrix[x])-1):
            i = x
            j = y
            salir = False
            while not salir: 
                i -= 1
                j += 1
                if (i >= 0 and j < len(matrix[i])):
                    if (matrix[i][j]=="#"):
                        salir = True
                        total += 1
                    if (matrix[i][j]=="L"):salir=True
                else:
                    salir = True
        # Vertical arriba
        i = x
        j = y
        salir = False
        while not salir: 
            i -= 1
            if (i >= 0):
                if (matrix[i][j]=="#"):
                    salir = True
                    total += 1
                if (matrix[i][j]=="L"):salir=True
            else:
                salir = True
    # Miro la fila de abajo
    if (x < len(matrix)-1):
        if (y>0): #Diagonal abajo izquierda
            i = x
            j = y
            salir = False
            while not salir:
                i += 1
                j -= 1
                if (i < len(matrix) and j >= 0):                    
                    if (matrix[i][j]=="#"):
                        salir = True
                        total += 1
                    if (matrix[i][j]=="L"):salir=True
                else:
                    salir = True

        if (y < len(matrix[x])-1): # Diagonal abajo derecha
            i = x
            j = y
            salir = False
            while not salir: 
                i += 1
                j += 1
                if (i < len(matrix) and j < len(matrix[i])):
                    if (matrix[i][j]=="#"):
                        salir = True
                        total += 1
                    if (matrix[i][j]=="L"):salir=True
                else:
                    salir = True
        #Hacia abajoa
        i = x
        j = y
        salir = False
        while not salir:
            i += 1
            if (i < len(matrix)):
                if (matrix[i][y]=="#"):
                    salir = True
                    total += 1
                if (matrix[i][y]=="L"): salir = True
            else:
                salir = True

    # Miro a la izquierda
    if (y > 0):
        i = y
        salir = False
        while not salir:
            i -= 1
            if (i >= 0):
                if (matrix[x][i]=="#"):
                    salir = True
                    total += 1
                if (matrix[x][i]=="L"):salir=True
            else:
                salir = True
    # Miro a la derecha
    if (y < len(matrix[x])-1):
        j = y
        salir = False
        while not salir:
            j += 1
            if (j < len(matrix[x])):
                if (matrix[x][j]=="#"):
                    salir = True
                    total += 1
                if (matrix[x][j]=="L"): salir=True
            else:
                salir = True
    return total

def step(matrix):
    tmp = []
    cambios = 0
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            item = matrix[i][j]
            c = count_occupied((i,j),matrix)
            if (matrix[i][j] == "L" and c == 0):
                item = "#"
                cambios += 1
            if (matrix[i][j] == "#" and c >= 5):
                item = "L"
                cambios += 1

            row.append(item)
        tmp.append(row)
    return (cambios,tmp)

def total_occupied(matrix):
    total = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j]=="#"):
                total += 1
    return total

def imprimir(matrix):
    for l in matrix:
        print(l)

matrix = load()
cambios = 1
while (cambios > 0):
    cambios,matrix = step(matrix)
    #imprimir(matrix)

print(total_occupied(matrix))
