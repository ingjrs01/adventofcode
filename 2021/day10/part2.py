def valores(letra):
    if (letra == '('):
        return 1

    if (letra == '['): 
        return 2

    if (letra == '{'):
        return 3

    if (letra == '<'):
        return 4

    return 0


def emparejan(i,j):
    if (i == "[" and j == "]"):
        return True
    if (i == "(" and j == ")"):
        return True
    if (i == "<" and j == ">"):
        return True
    if (i == "{" and j == "}"):
        return True
    return False

def process_line(line):
    stack = []
    for i in range(len(line)):
        #print(line[i])
        if (line[i] in ['(','[','<','{']):
            stack.append(line[i])
        if (line[i] in [')',']','>','}']):
            p = stack.pop()
            if (emparejan (p,line[i])):
                continue
            else:
                return 0
    ## la línea está incompleta, calculo
    total = 0
    while(len(stack)>0):
        letra = stack.pop()
        total = total * 5
        total += valores(letra)
    
    return total


lines = open('real','r').readlines()
totales = []
for line in lines: 
    t_line = process_line(line)
    if (t_line > 0):
        totales.append(t_line)
    #print("************************************************************")

medio = (len(totales)//2) 
ordenados = sorted(totales)
print(ordenados)
print(medio)
print(ordenados[medio])
