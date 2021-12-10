def valores(letra):
    if (letra == ')'):
        return 3

    if (letra == ']'): 
        return 57

    if (letra == '}'):
        return 1197

    if (letra == '>'):
        return 25137

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
                return (valores(line[i]))
    
    return 0


lines = open('real','r').readlines()
total = 0
for line in lines: 
    total += process_line(line)
    #print("************************************************************")
print(total)
