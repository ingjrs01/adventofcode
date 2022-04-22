import sys
def run(data): 
    pos = 0

    while (pos < len(data)): 
        if (data[pos] == 99): 
            return data
        if (data[pos] == 1):
            data[data[pos + 3]] = data[data[pos + 1]] + data[data[pos+2]]
        if (data[pos] == 2):
            data[data[pos + 3]] = data[data[pos + 1]] * data[data[pos+2]]
        pos += 4

    return data

def process_file(filename):
    line = open(filename).readline()
    data =[int(x) for x in line.split(",")]
    data[1] = 12
    data[2] = 2
    print(line)
    print ("Data: ")
    print (data)
    return data

filename='input'
if (len(sys.argv) > 1):
    filename = str(sys.argv[1])

datos = process_file(filename)
#print("--------------------")
for i in range(100):
    for j in range(100):
        data_tmp = datos.copy()
        data_tmp[1] = i
        data_tmp[2] = j
        datos2 = run(data_tmp)
        if datos2[0] == 19690720: 
            print ("Encontrado:  i: " + str(i) + " j: " + str(j))
            print("Solución: " + str(100 * i + j) )
            break

#datos2 = run(datos)
print(datos2)
