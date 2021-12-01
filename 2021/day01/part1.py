data = [int(i) for i in open('input','r').readlines()]
t = len(data)
cont = 0
for i in range(t-1):
    if (data[i+1]>data[i]):
        cont += 1

print(cont)
