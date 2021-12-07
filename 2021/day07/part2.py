class Costes(): 
    def __init__(self):
        self.costes ={}
        self.costes[0]=0
        self.costes[1]=1
                
    def c(self,val):
        print("Quiero calcular " + str(val))
        if (val in self.costes.keys()):
            print("Encontrado" + str(self.costes[val]))
            return (self.costes[val])
        
        for i in range(max(self.costes.keys())+1,val+1):
            self.costes[i] = self.costes[i-1] + i 

        return self.costes[val]

    def imprimit(self):
        print(self.costes)
        


def resta(v1,v2):
    if (v1 > v2):
        return v1 - v2

    return v2 - v1


input = [16,1,2,0,4,2,7,1,2,14,20]

input = [int(i) for i in open('input','r').readline().strip().split(",")]

data = {}
costes = Costes()
costes.imprimit()

for i in range(max(input)):
    total = 0
    for j in input:
        total += costes.c(resta(i,j))
    data[i] = total 

print(data)
print("Costes:")
costes.imprimit()
print("-----")
res = min(data,key=data.get)
print(res)
print(data[res])
