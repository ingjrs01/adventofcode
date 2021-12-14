def load(filename):
    lines = [l.strip() for l in open(filename,'r').readlines()]
    pattern = lines [0] # first line is pattern

    rules = {}
    for line in lines[2:]:
        a,b = line.split(" -> ")
        rules[a] = b
    return pattern,rules

def iteration(steps,input,rules):
    # look input at two chars once
    pares = {}
    letters = {}
    for i in range(len(input)-1):
        par = input[i] + input[i+1]
        if par not in pares: pares[par]=0
        pares[par] += 1
        if input[i] not in letters: letters[input[i]] = 0
        letters[input[i]] += 1
    if input[-1] not in letters: letters[input[-1]]=0
    letters[input[-1]] += 1
    for i in range(steps):
        nuevos_pares = {}
        for par in pares:
            # miro si está en rules:
            r = rules[par]
            if par[0] + r not in nuevos_pares: nuevos_pares[par[0]+r]=0
            nuevos_pares[par[0]+r] += pares[par] 

            if r + par[1] not in nuevos_pares: nuevos_pares[r + par[1]]=0
            nuevos_pares[r + par[1]] += pares[par] 
            # Proccess letters individually
            if r not in letters:letters[r]=0
            letters[r] += pares[par]
        pares = nuevos_pares
    return letters
                
data,rules = load('real')
letters = iteration(40,data,rules)
r = max(letters.values()) - min(letters.values())
print(r)
