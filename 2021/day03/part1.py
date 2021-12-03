lines = open('input','r').readlines()
size_linea = 12
unos = [0,0,0,0,0,0,0,0,0,0,0,0]

for line in lines:
    for i in range(size_linea):
        if (line[i] == '1'):
            unos[i] += 1

media = len(lines)/2
gamma   = 0
epsilon = 0

for i in range(size_linea):
    if (unos[i] > media):
        gamma += 2**(size_linea - (i+1))
    else:
        epsilon += 2**(size_linea - (i+1))

print(gamma)
print(epsilon)
print(gamma*epsilon)
