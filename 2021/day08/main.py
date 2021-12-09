
lines = open('input','r')

def part1():
    tam = [2,3,4,7]
    total = 0
    for line in lines:
        #print (line)
        words = line.split("|")[1].split()
        print(words)
        for w in words:

            if (len(w) in tam):
                print(w) 
                total += 1

    print(total)

def transform(t):
    temp = [s.strip() for s in t.split()]
    words = []
    #print(temp)
    for w in temp:
        words.append("".join( sorted(w)))
    return (words)

def detect_a(one,seven):
    #print("Uno " + one)
    #print("Siete " + seven)
    return (seven.replace(one[0],"").replace(one[1],""))

def detect_five(entry,letras,four,one,eight,diccionario):
    candidatos = []
    for w in entry:
        if (len(w) == 5):
            candidatos.append(w)
    comunes = []
    for i in range(len(candidatos[0])):
        if ((candidatos[0][i] in candidatos[1]) and (candidatos[0][i] in candidatos[2])):
            comunes.append(candidatos[0][i])

    print(comunes)
    for l in comunes:
        if l in four:
            letras["d"] = l

    letras["b"] = four.replace(letras["d"],"").replace(one[0],"").replace(one[1],"")
    five = ""
    for w in candidatos: 
        if (letras["b"] in w):
            five = w
            diccionario[w] = 5
            #print("El cinco es: " + w)
    # 5 y 1 tienen en común f
    if (one[0] in five):
        letras['f'] = one[0]
        letras['c'] = one[1]
    else:
        letras['f'] = one[1]
        letras['c'] = one[0]
    # Al 5 le quito todas las letras que ya conozco
    letras['g'] = five.replace(letras['a'],'').replace(letras['b'],'').replace(letras['d'],'').replace(letras['f'],'')
    #print(candidatos)
    letras['e'] = eight.replace(letras['a'],'').replace(letras['b'],'').replace(letras['c'],'').replace(letras['d'],'').replace(letras['f'],'').replace(letras['g'],'')

    three = "".join( sorted([letras['a'],letras['c'],letras['d'],letras['f'],letras['g']]))
    diccionario[three] = 3

    six = "".join(sorted([letras['a'],letras['b'],letras['d'],letras['e'],letras['f'],letras['g']]))
    diccionario[six] = 6

    two = "".join(sorted([letras['a'],letras['c'],letras['d'],letras['e'],letras['g']]))
    diccionario[two] = 2

    nine = "".join(sorted([letras['a'],letras['b'],letras['c'],letras['d'],letras['f'],letras['g']]))
    diccionario[nine] = 9

    zero = "".join(sorted([letras['a'],letras['b'],letras['c'],letras['e'],letras['f'],letras['g']]))
    diccionario[zero] = 0





print("segunda parte")
total = 0
for line in lines:
    print(line)
    tnumeros,tsalida = line.split("|")
    numeros = transform(tnumeros)
    print(numeros)
    diccionario = {}
    letras = {}
    # Primera deteccion
    one = ""
    seven = ""
    four = ""
    eight = ""
    for n in numeros:
        if (len(n) == 2):
            diccionario[n] = 1
            one = n
        if (len(n) == 3):
            seven = n
            diccionario[n] = 7
        if (len(n) == 4):
            four = n
            diccionario[n] = 4
        if (len(n) == 7):
            eight = n
            diccionario[n] = 8
    letras["a"] = detect_a(one,seven)
    detect_five(numeros,letras,four,one,eight,diccionario)

    print(letras)
    print(diccionario)
    print("Descifrando")
    ## Descifro la salida:
    salida = transform(tsalida)
    numero = diccionario[salida[0]] * 1000 + diccionario[salida[1]] * 100 + diccionario[salida[2]] * 10 + diccionario[salida[3]]
    total += numero
    print(numero)
    print ("*******************************************************")

print(total)

