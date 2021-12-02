
lines = open('input','r').readlines()
x = 0
y = 0

for line in lines:

    parts = line.split()
    print(parts[0] + " -> " + parts[1])

    if (parts[0] == "forward"):
        x += int(parts[1])
    if (parts[0] == "up"):
        y -= int(parts[1])
    if (parts[0] == "down"):
        y += int(parts[1])

print("Valor de x " + str(x) )
print("valor de y " + str(y))
print("Resultado = " + str(x*y))
