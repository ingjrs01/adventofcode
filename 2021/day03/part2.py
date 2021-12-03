def removelines(lines, value,pos):
    newlines = []
    for line in lines:
        if (line[pos] == value):
            newlines.append(line)

    return (newlines)

def analize(lines,pos,param):
    unos = 0
    ceros = 0

    for line in lines:
        if (line[pos] == '1'):
            unos += 1
        else:
            ceros += 1
    if (param == 'o'):
        if (unos >= ceros):
            return '1'
        
        return '0'
    else:
        if (ceros <= unos):
            return '0'
        else:
            return '1'

def tobin(num):
    num = num.strip()
    val = 0
    size = len(num)
    for i in range(size):
        val += int(num[i]) *  2**(size - (i+1))
    return val

def oxigen(lines,param):
    size_linea = len(lines[0])
    linesaux = lines

    for i in range(size_linea):
        res = analize(linesaux,i,param)
        linesaux = removelines(linesaux,res,i)
        if (len(linesaux)== 1):
            return linesaux[0]

# Main 
lines = open('input','r').readlines()
o =  tobin ( oxigen(lines,'o'))
c =  tobin ( oxigen(lines,'c'))
print(o)
print(c)
print(o*c)

