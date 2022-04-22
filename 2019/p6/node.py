# Nodo de un arbol no binario

class Node():
    def __init__(self,parent,val):
        self.value = val
        self.parent = parent
        self.children = []
        if parent is not None: 
            parent.addChild(self)
    
    def addChild(self,child): 
        self.children.append(child)

    def depth(self): 
        p = 0
        actual = self
        while actual.parent is not None:
            actual = actual.parent
            p += 1        
        return p

    def search(self,tree,val):
        print("Buscando...")
        print(tree)
        print("Valor: " + val)

        if tree.value == val: 
            print("Valor Encontrado")
            return tree

        # busco en sus hijos
        for actual in tree.children:
            actual.search(actual,val)

        return None

    def __str__(self) -> str:
        s = ""
        s += "Valor: " + self.value
        s += ", Hijos: " + str(len(self.children))
        s += ", Profundidad" + str(self.depth())
        for hijo in self.children:
            s += " > " + str(hijo)

        return s

class Tree(): 
    def __init__(self):
        self.node = Node(None,"Tree")

    # Añadimos un nodo sabiendo el id del padre, y el valor del hijo
    def addChild(self, parentval, nodeval):
        parent = self.node.search(self.node,parentval)
        print ("Acabo de buscar al padre y es: ")
        print(parent)
        if parent is None:
            print("No se encuentra padre")
            return False

        node = Node(parent,nodeval)
        return True


    def __str__():
        return ""
    
    def travel(self): 
        return 0

abuelo = Tree()
abuelo.addChild("Tree","Nicanor")
print("Primero insertado")
abuelo.addChild("Nicanor","Juan")
#abuelo.addChild("Juan","Juan Ramón")
#abuelo.addChild("Juan","Sara")
#abuelo.addChild("Juan Ramón","Breixo")
#abuelo.addChild("Juan Ramón","Manuel")
#abuelo.addChild("Juan Ramón","Lola")

#jr = abuelo.search(abuelo,"Juan Ramón")
#print(jr)

##juan = Node(abuelo,"Juan")
##jr = Node(juan,"Juan Ramón")
##sara = Node(juan,"Sara")
##manuel = Node(jr,"Manuel")
##breixo = Node(jr,"Breixo")
##lola = Node(jr,"Loliña")

#abuelo.addChild(juan)
#juan.addChild(jr)
#juan.addChild(sara)

#print(manuel)
#print(juan)
