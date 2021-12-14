

def load(filename):
    lines = [s.strip() for s in open(filename,'r').readlines()]
    time = int(lines[0])
    busses = [int(value) for value in lines[1].split(",") if value != "x"]

    return time,busses


t,busses = load("input")
print(f"Tiempo buscado {t}");
print(busses)

for i in range(t,t+1000):
    for bus in busses:
        if (i % bus) == 0:
            print(f"Hemos encontrado {i} el bus {bus})")
            print(f"Resultado: {(i - t) * bus}")
            exit(0)
