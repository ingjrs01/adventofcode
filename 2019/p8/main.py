# Cuantas veces hay num en data. 
def contar(data,num): 
    j = 0 
    for i in data: 
        if i == num: 
            j += 1
    return j

def load_data(filename):
    f = open('input')
    line = f.readline().strip()

    data = []
    for i in range(0,len(line)):
        data.append(int(line[i]))
    return data

# Divide los datos en capas. Cada capa es una posición del array
def load_layers(data): 
    ini = 0
    tam = 150
    fin = 150
    tam_array = len(data)
    vueltas = int(tam_array/tam)

    print("Tamaño de los datos: " + str(tam_array))
    print("Vueltas: " + str(vueltas))

    layers = []
    for i in range(vueltas):
        fin = ini + tam
        if tam > tam_array:
            tam = tam_array - 1
        print("ini: " + str(ini) + "  fin: " + str(fin) + "  layer: " + str(i))
        layers.append(data[ini:fin])
        ini += tam
        print(layers[i])
        print("")
    return layers

def result_part_1(layers): 
    minimo = 999
    minimo_index = -1
    unos = 0
    doses = 0
    mult = 0

    for layer in layers: 
        ceros = contar(layer,0)
        if ceros < minimo:
            minimo = ceros 
            unos = contar(layer,1)
            doses = contar(layer,2)
            mult = unos * doses

    print ("El mínimo de ceros es: " + str(minimo))
    print ("El número de unos: " + str(unos))
    print ("El número de doses: " + str(doses))
    print ("Resultado final: " + str(mult))

# Cada fila de layers es una capa, y cada número un pixel, de forma que: 
# 0 -> Negro, 1 -> Blanco, 2 -> transparente
def result_part_2(layers): 
    layer_final = []
    for i in range(0,150):  # Voy revisando todas las capas
        for j in range(0,99): 
            #print(str(i) + "  Pixel = " + str(layers[j][i]))
            if layers[j][i] != 2:
                pixel = layers[j][i]
                break
        layer_final.append(pixel)

    return (layer_final)

def print_message(data): 
    for i in range(6):
        for j in range(25):
            #print(str(i) + " " + str(j))
            if data[j + i * 25] == 0:
                c = "⬛"
            else:
                c = " "
            print(c, end = '')
        print("")


## Programa Principal: 

data = load_data('input')
layers = load_layers(data)
result_part_1(layers)
print ("Pintamos capas --------------------------------------------------------------------------------")
for layer in layers: 
    print (layer[0:35])
msg = result_part_2(layers)
print(msg)
print(len(msg))
print (msg[0:25])
print (msg[25:50])
print (msg[50:75])
print (msg[75:100])
print (msg[100:125])
print (msg[125:])

print_message(msg)
