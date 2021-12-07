lines = open('input','r').readlines()

rules = {}

for line in lines:
    parts = line.strip()[:-1].split('contain')
    children = []
    if (parts[1].strip() == "no other bags"):
        pass
    else:
        for c in [s.strip() for s in parts[1].split(",")]:
            num = int(c[:1])
            text = c[1:].strip()
            if (num == 1):
                text += "s"

            children.append( (num,text))
    rules[parts[0].strip()] = children

print (rules)

input = [(1,"shiny gold bags")]

print("*******************************************************************")
total = -1 # Para descontar la bolsa original
while (len(input)>0):
    item = input.pop(0)
    total += item[0] 
    for h in rules[item[1]]:
        #:wq        print(h)
        input.append((item[0]*h[0],h[1]))

    print(input)
    print(total)
    print("***********************************************************")
print (total)
