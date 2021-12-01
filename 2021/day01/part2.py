print("Advent of code 2021")

f = open('input2.txt',"r")

cont = 0
data = [int (a.strip()) for a in f.readlines()]

anterior = data[0] + data[1] + data[2]

tamp = len(data)
print(tamp)
for i in range(1,tamp):
    if (i + 2 < tamp):
        val = data[i] + data[i+1] + data[i+2]
        if (val > anterior):
            cont += 1

        anterior = val

print(cont)
