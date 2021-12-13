import networkx as nx
from treelib import Node, Tree

def load(filename):
    rules = [s.strip() for s in open(filename,'r').readlines()]

    g = nx.Graph()
    for rule in rules:
        a,b = rule.split("-")
        if (a not in list(g.nodes())):
            g.add_node(a)
        if (b not in list(g.nodes())):
            g.add_node(b)
        g.add_edge(a,b)
    
    return g

def recorrer(g):
    caminos = []
    pendientes = []
    tree = Tree()
    tree.create_node("start","start")

    for item in list(g.adj["start"]):
        pendientes.append(item)

    camino = []
    while(len(pendientes)>0):
        print(pendientes)
        nodo = pendientes.pop(0)
        print(nodo)
        camino.append(nodo)
        
        n = tree.create_node(nodo,parent="start")
        print(list(g.adj[nodo]))
        print(n.ancestors())
        print("Fin de este camino-----------------------------------------------------")
    
    tree.show()
    return caminos

g = load('input')

caminos = recorrer(g)

print(len(caminos))
