
data = [int(i) for i in open('real','r').readlines()]
data.append(0)
data.sort()
print(data)

diferencias=[]
for i in range(len(data)-1):
    diferencias.append(data[i+1]-data[i])

unos = diferencias.count(1)
tres = diferencias.count(3) + 1
print(unos)
print(tres)
print(unos*tres)

print("Segunda parte")

tmp = {}
tmp[0] = 1
fin = []

maximo = data[len(data)-1]
print("Maximo: " + str(maximo))
while (len(tmp)>0):
#for j in range(10):
    actual = list(tmp.keys())[0]
    value = tmp.pop(actual)
    print("Valor quitado " + str(actual))
    print("Número de veces: " + str(value))
    #actual = tmp.pop(list(tmp.keys())[0])
    if (actual==maximo):
        fin.append(actual)
        continue
    cont = 0
    if (actual+1 in data):
        k = actual + 1
        if (k in tmp.keys()):
            tmp[k] += value
        else:
            tmp[k] = value
    if (actual +2 in data):
        k = actual + 2
        if (k in tmp.keys()):
            tmp[k] += value
        else:
            tmp[k] = value
    if (actual + 3 in data):
        k = actual + 3
        if (k in tmp.keys()):
            tmp[k] += value
        else:
            tmp[k] = value

    print(tmp)
    print("------------------------------------------------------")

print(len(fin))