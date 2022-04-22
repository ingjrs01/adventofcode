

numbers = [int(i) for i in open('input2.txt').readline().split(",")]

print(numbers)
print("------------------------------------")
tam = 30000000
nuevo = 0
#tam = 10
ini = len(numbers)
for i in range(ini,tam):
    #print("###############################################")
    #print("Turno: " + str(i+1) + " ",end="")
    #print(numbers, end="")
    if (numbers[i-1] in numbers[:-1]):
        #print("Repetido:")
        #print(" buscado: " + str(numbers[i-1]) + ": ", end="")
        l = numbers[:-1]
        pos = l[::-1].index(numbers[i-1])
        #print("pos: " + str(pos))
        #print(i - pos)
        p = ((i-1) - pos)
        #print("Ultima posición: " + str(i))
        #print("Primera posición: " + str(p))
        nuevo = i - p
        
        #pos = numbers[:-1].reverse().index(numbers[i-1])
        #print(pos)
    else:
        nuevo = 0

    #print("Nuevo: " + str(nuevo))
    numbers.append(nuevo)
print(nuevo)
#print(numbers)