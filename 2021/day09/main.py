
def search_low(matrix):
    positions = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (j > 0):
                if (matrix[i][j] >= matrix[i][j-1]):
                    continue
            if (j < len(matrix[i])-1):
                if (matrix[i][j] >= matrix[i][j+1]):
                    continue
            if (i > 0):
                if (matrix[i][j] >= matrix[i-1][j]):
                    continue
            if (i < len(matrix)-1):
                if (matrix[i][j] >= matrix[i+1][j]):
                    continue

            positions.append((i,j))
    return positions

def f_in(p,m):
    for e in m:
        if (e[0] == p[0] and e[1] == p[1]):
            return True
    return False



def calc_basin(matrix,coords):
    # Nos pasan una coordenada, y calculo el tamaño del basin
    pendientes = []
    finalizados = []

    pendientes.append((coords[0],coords[1]))
    while (len(pendientes)>0):
        actual = pendientes.pop(0)
        if (actual[1] > 0):
            if (matrix[actual[0]][actual[1]-1] != 9):
                if (f_in((actual[0],actual[1]-1),pendientes) == False and f_in((actual[0],actual[1]-1),finalizados)==False):
                    pendientes.append((actual[0],actual[1]-1))
        if (actual[1] < len(matrix[actual[0]])-1):
            if (matrix[actual[0]][actual[1]+1] != 9):
                if (f_in((actual[0],actual[1]+1),pendientes)==False and f_in((actual[0],actual[1]+1),finalizados)==False):
                    pendientes.append((actual[0],actual[1]+1))
        if (actual[0] > 0):
            if (matrix[actual[0]-1][actual[1]] != 9):
                if (f_in((actual[0]-1,actual[1]),pendientes)==False and f_in((actual[0]-1,actual[1]),finalizados)==False):
                    pendientes.append((actual[0]-1,actual[1]))
        if (actual[0] < len(matrix)-1):
            if (matrix[actual[0]+1][actual[1]] != 9):
                if (f_in((actual[0]+1,actual[1]),pendientes)==False and f_in((actual[0+1],actual[1]),finalizados)==False):
                    pendientes.append((actual[0]+1,actual[1]))
    
        if (f_in(actual,finalizados)==False):
            finalizados.append(actual)
    return (len(finalizados))




matrix = []
lines = open('real','r').readlines()

for line in lines:
    row = []
    l = line.strip()
    for i in range(len(l)):
        row.append(int(l[i]))
    matrix.append(row)

positions = search_low(matrix)
total = 0
for p in positions: 
    valor = matrix[p[0]][p[1]] + 1
    total += valor


print(total)
tams = []
print("Segunda parte")
for p in positions:
    tams.append(calc_basin(matrix,p))

la = sorted(tams)
t = len(la)-1
resultado = la[t] * la[t-1] * la[t-2]
print(resultado)
