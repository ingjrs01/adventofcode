lines = open('input','r').readlines()
x = 0
y = 0
aim = 0

for line in lines:

    parts = line.split()
    if (parts[0] == "forward"):
        x += int(parts[1])
        y += aim * int(parts[1])
    if (parts[0] == "up"):
        aim -= int(parts[1])
    if (parts[0] == "down"):
        aim += int(parts[1])

print("Resultado = " + str(x*y))
