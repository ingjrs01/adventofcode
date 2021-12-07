

d = {}
d[1] = 2
d[2] = 3

while(len(d)>0):
    d.pop(list(d.keys())[0])
    print(d)
    print(len(d))