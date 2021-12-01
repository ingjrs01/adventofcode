print("Advent of code 2021")

f = open('input.txt',"r")

ant = int( f.readline())
cont = 0
for line in f.readlines():
    try:
        nuevo = int(line)
        print(nuevo)
        if (nuevo > ant):
            cont += 1
        ant = nuevo
    except:
        print("Valor no válido")

print(cont)



