from octupus import Octopus

def load():
    lines = [line.strip() for line in open('real','r').readlines()]
    data = []
    x = 0
    for l in lines:
        row = []
        for i in range(len(l)):
            row.append(Octopus(int(l[i]),x,i))
        data.append(row)
        x += 1
    # Una vez creados, le pongo los vecinos a todos
    for x in range(10):
        for y in range(10):
            coords = data[x][y].getNeighbors()
            neighbors = []
            for p in coords:
                neighbors.append(data[p[0]][p[1]])
            data[x][y].setNeighbors(neighbors)
                
    return(data)

data = load()
flashes  = 0
for i in range(1000):
    for x in range(10):
        for y in range(10):
            data[x][y].step()

    for x in range(10):
        for y in range(10):
            data[x][y].check()

    flash_step = 0
    for x in range(10):
        for y in range(10):    
            if (data[x][y].getVal()==0):
                flash_step += 1
            print(data[x][y].getVal(),end='')
        print("")
    flashes += flash_step
    print(flashes)
    print(i)
    if flash_step == 100:
        break
    print("************************************************")
