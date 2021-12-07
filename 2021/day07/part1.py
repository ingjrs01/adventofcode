
def resta(v1,v2):
    if (v1 > v2):
        return v1 - v2

    return v2 - v1


input = [16,1,2,0,4,2,7,1,2,14]

input = [int(i) for i in open('input','r').readline().strip().split(",")]

data = {}

#data[4] = "hola"

for i in range(max(input)):
    total = 0
    for j in input:
        total += resta(i,j)
    data[i] = total 

print(data)
res = min(data,key=data.get)
print(res)
print(data[res])
