from treelib import Node, Tree

def search_in_trees(arboles,padre):
    for arbol in arboles.values():
        node = arbol.get_node(padre)
        if node is not None: 
            return arbol

    return None

f = open('input')
lines = f.readlines()
comandos =  []
for line in lines: 
    comandos.append(line)

arboles = {}  # Es un diccionario, para poder acceder por índice
for comando in comandos: 
    padre,hijo = comando.strip().split(")")
    
    if hijo in arboles.keys():
        # Todavía tengo que buscar al padre
        tree = search_in_trees(arboles,padre)
        if tree is not None:
            tree.paste(padre, arboles[hijo])            
            arboles.pop(hijo)
        else:
            # Hay que crear un árbol nuevo, y pegar el hijo en el
            tree = Tree()
            tree.create_node(padre,padre)
            tree.paste(padre,arboles[hijo])
            arboles[padre] = tree
            arboles.pop(hijo)
    else:
        # Inserción normal 
        tree = search_in_trees(arboles,padre)
        if tree is not None:
            tree.create_node(hijo,hijo,padre)
        else:
            tree = Tree()
            tree.create_node(padre,padre)
            tree.create_node(hijo,hijo,padre)
            arboles[padre] = tree

s = 0
for arbol in arboles.values():    
    #arbol.show()
    for node in arbol.expand_tree(mode=Tree.DEPTH):
        #print(node + "  " + str(tree.depth(node)))
        s += arbol.depth(node)
print ("Suma de profundidades: " + str(s))


# Busco ancestro común entre SAN y YOU
master_tree = arboles['COM']
#print (master_tree.depth())

node = master_tree.parent('YOU')
print ("Este es el array YOU")
you = []
while node is not None:
    #print(node.identifier)
    you.insert (0,node.identifier)
    node = master_tree.parent(node.identifier)
print (you)

node = master_tree.parent('SAN')
print ("Este es el array SAN")
san = []
while node is not None:
    #print(node.identifier)
    san.insert (0,node.identifier)
    node = master_tree.parent(node.identifier)
print (san)

j = 0
for i in you:
    if i != san[j]:
        print (j)
        break
    j += 1

print (len(you) + j)


