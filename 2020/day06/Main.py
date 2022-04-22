def read_input(filename):
    lines = open(filename).readlines()
    return lines

def part1():
    print("Primera parte")
    lines = read_input("input.txt")
    total = []
    entradas = {}
    for line in lines: 
        if (line == "\n"):
            total.append(sum(entradas.values()))
            #print(entradas)
            entradas = {}
        else: 
            for i in range(len(line)):
                letter = line[i]
                if (letter == "\n"):
                    continue
                if letter in entradas.keys():
                    entradas[letter] = 1
                else:
                    entradas[letter] = 1 
    total.append(sum(entradas.values()))
    print(entradas)
    print(total)
    print(sum(total))

def analizar(lineas,datos):
    print(datos)
    # Datos
    total = 0
    for elemento in datos.values(): 
        if (elemento == lineas):
            total += 1
    return total

def part2():
    print("Segunda parte")
    lines = read_input("input.txt")
    total = []
    entradas = {}
    c_lin = 0
    for line in lines: 
        if (line == "\n"):
            print("Total lineas " + str(c_lin))
            t = analizar(c_lin,entradas)
            total.append(t)
            #print(entradas)
            entradas = {}
            c_lin = 0
        else: 
            c_lin += 1
            for i in range(len(line)):
                letter = line[i]
                if (letter == "\n"):
                    continue
                if letter in entradas.keys():
                    entradas[letter] += 1
                else:
                    entradas[letter] = 1 
    t = analizar(c_lin,entradas)                
    total.append(t)
    #print(entradas)
    print(total)
    print(sum(total))


part2()