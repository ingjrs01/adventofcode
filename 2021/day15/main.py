import networkx as nx

def load(filename):
    tmp = [line.strip() for line in open(filename,'r').readlines()]
    data = []
    for line in tmp:
        row = []
        for i in range(len(line)):
            row.append(int(line[i]))
        data.append(row)
    return data

def to_graph(data):
        g = nx.Graph()
        for i in range(len(data)):
            for j in range(len(data[i])):
                node = (i,j) #(i*10+j)
                g.add_node(node)
        # Metiendo las aristas:
        for i in range(len(data)):
            for j in range(len(data[i])):
                l = get_adjacents(data,(i,j))
                #print((i,j),end="")
                #print(l)
                n1 = (i,j)#i*10+j
                for node in l:
                    n2 = (node[0],node[1])#node[0]*10 + node[1]
                    g.add_edge(n1,n2,weight=node[2])
        return g

def get_adjacents(data,pos):
    positions = []

    if (pos[0] < len(data)-1):
        positions.append((pos[0]+1,pos[1],data[pos[0]+1][pos[1]]))

    if (pos[1] < len(data[pos[0]])-1):
        positions.append((pos[0],pos[1]+1,data[pos[0]][pos[1]+1]))

    return positions


data = load('input')
g = to_graph(data)
#print(list(g.nodes))

#print(get_adjacents(data,(9,9)))
path=nx.dijkstra_path(g, source=(0,0), target=(99,99))
path2=nx.dijkstra_path_length(g, source=(0,0), target=(99,99))
print(path2)
total = 0
for n in path:
    #print("Nodo: ",end='')
    #print(n,end="")
    i = int(n[0])
    j = int(n[1])
    #print(data[i][j])
    total += data[i][j]
print(total)
