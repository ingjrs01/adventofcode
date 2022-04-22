def read_input(filename):
    lines = open(filename).readlines()
    return lines

def bin_2_dec(input):
    val = 0
    index = 0 
    for letter in input[::-1]:
        val += int(letter) * 2**index
        index += 1
    return (val)

def calculate_site(i):
    #v = i[:7].replace("F","0").replace("B","1")
    row = bin_2_dec(i[:7].replace("F","0").replace("B","1"))
    column = bin_2_dec(i[-3:].replace("R","1").replace("L","0"))
    solution = row * 8 + column
    return solution

def part1():
    max_ = 0
    lines = read_input("input.txt")
    for line in lines: 
        actual = calculate_site(line.rstrip())
        if (actual > max_):
            max_ = actual
    print ("El número máximo es: " + str(max_))

def part2():
    tam = 862 # La solución de la parte 1
    valores = []
    for i in range(tam): 
        valores.append(0)
    print(valores)
    lines = read_input("input.txt")
    for line in lines: 
        actual = calculate_site(line.rstrip())
        print(actual)
        valores[actual] = 1
    print(valores)
    for i in range(tam): 
        if (valores[i] == 0):
            print(i)

part2()
