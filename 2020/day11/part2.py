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
            if (matrix[x-1][y-1]=="#"):
                total += 1
        if (y < len(matrix[x])-1):
            if (matrix[x-1][y+1]=="#"):
                total += 1
        if (matrix[x-1][y]=="#"):
            total += 1
    # Miro la fila de abajo
    if (x < len(matrix)-1):
        if (y>0):
            if (matrix[x+1][y-1]=="#"):
                total += 1
        if (y < len(matrix[x])-1):
            if (matrix[x+1][y+1]=="#"):
                total += 1
        if (matrix[x+1][y]=="#"):
            total += 1
    # Miro la fila actual
    if (y > 0):
        if (matrix[x][y-1]=="#"):
            total += 1
    if (y < len(matrix[x])-1):
        if (matrix[x][y+1]=="#"):
            total += 1
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
            if (matrix[i][j] == "#" and c >= 4):
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


matrix = load()
cambios = 10
while (cambios > 0):
    cambios,matrix = step(matrix)
    print(total_occupied(matrix))
