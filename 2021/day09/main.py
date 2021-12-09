
def search_low(matrix):
    positions = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            #print(f"Posición ({i},{j}) = {matrix[i][j]}")
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

def calc_basin(coors):
    # Nos pasan una coordenada, y calculo el tamaño del basin



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




