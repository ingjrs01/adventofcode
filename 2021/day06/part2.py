
values = [int(i) for i in open('input','r').readline().split(",")]

data = [0,1,2,3,4,5,6,7,8,9]

steps = 256

for i in range(10):
    data[i] = values.count(i)

for i in range(steps):
    item = data.pop(0)
    data[6] += item
    data[8] = item
    data.append(0)

print(sum(data))
    
