
def load(filename):
    lines = open(filename,'r').readlines()
    data = []
    coords = []
    max_x = 0
    max_y = 0
    for line in lines:
        if ('fold' in line):
            continue
        
        if (line == "\n"):
            continue
        x,y = line.strip().split(",")
        x,y = int(x),int(y)
        if (x > max_x):
            max_x = x
        if (y > max_y):
            max_y = y

        coords.append((x,y))
    max_x += 1
    max_y += 1

    for i in range(max_y):
        row = []
        for j in range(max_x):
            row.append(False)
        data.append(row)

    for c in coords:
        # print(f"Coordenadas: ({c[1]},{c[0]})")
        data[c[1]][c[0]] = True

    return data

def plegar_y(data,p):
    tmp = []
    for i in range(p):
        row = []
        for j in range(len(data[0])):
            row.append(data[i][j])
        tmp.append(row)

    k = p
    for i in range(p-1,-1,-1):
        k += 1
        tt = len(data)
        if (k >= len(data)):
            break
        for j in range(len(data[0])):
            tmp[i][j] = data[i][j] or data[k][j]

    return (tmp)

def plegar_x(data,p):
    tmp = []
    tam = len(data[0])
    for i in range(len(data)):
        row = []
        for j in range(p):
            k = (tam - (1 + j))

            row.append(data[i][j] or data[i][k])
        tmp.append(row)


    return (tmp)


data = load('input2')
#data = plegar_y2(data,5)
#data = plegar_x(data,5)
data = plegar_x(data,655)
data = plegar_y(data,447)

contar = 0
for i in data:
    for j in i:
        if (j):
            contar += 1


print(contar)
data = plegar_x(data,327)
data = plegar_y(data,223)
data = plegar_x(data,163)
data = plegar_y(data,111)
data = plegar_x(data,81)
data = plegar_y(data,55)
data = plegar_x(data,40)
data = plegar_y(data,27)
data = plegar_y(data,13)
data = plegar_y(data,6)

print("And de winner is")
for i in data:
    for j in i:
        if (j):
            print("#",end="")
        else:
            print(".",end="")
    print("")
