

def load(filename):
    lines = [s.strip() for s in open(filename,'r').readlines()]
    items = lines[1].split(",")
    busses = {}
    i = 0
    for item in items:
        if (item != "x"): busses[int(item)] = i
        i += 1 

    return busses


busses = load("input")
print(busses)

ini = 100000000000000
#ini = 1000000
#incremento = product(busses.keys())
incremento = 37 * 41 * 601 * 19 * 17 * 23 * 29 * 443 * 13
print(f"Incremento: {incremento}")
#Busco primer contacto
for i in range(ini,ini+incremento):
    if (i % incremento) == 0:
        print(f"Encontrado {i}")
        break
for j in range(i,i+7000000000000,incremento):
    #print(f"Numéro {j} modulo {j%incremento} --- {j-busses[incremento]}")
    t = j - busses[incremento]
    encontrado = True
    for bus in busses.keys():
        #print(f"{bus} -> {t + busses[bus]}   =  {(t + busses[bus])% bus}")
        if (((t + busses[bus]) % bus) != 0):
            encontrado = False
    if encontrado:
        print(t) 
        exit(0)

exit(0)
while True:
    i += incremento
    for bus in busses.keys():
        print(f"Busco i")
        if ((i + busses[bus]) % bus  != 0): break
    print(f"Hemos encontrado a i: {i}")
    exit(0)
