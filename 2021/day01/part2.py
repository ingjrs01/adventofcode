data = [int (a.strip()) for a in open('input','r').readlines()]
cont = 0

previous = data[0] + data[1] + data[2]

size = len(data)
for i in range(1,size):
    if (i + 2 < size):
        val = data[i] + data[i+1] + data[i+2]
        if (val > previous):
            cont += 1

        previous = val

print(cont)
