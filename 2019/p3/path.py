from point import Point

class Path(): 
    def __init__(self,s): 
        self.nodes = []
        self.processPath(s)

    def processPath(self,s):
        lastNode = Point(0,0)
        commands = s.split(",")
        for command in commands:             
            nodes = self.getNodesFromCommand(lastNode,command)
            if len(nodes) > 0: 
                for n in nodes:
                    self.nodes.append(n)
                lastNode = nodes[-1]

    def getNodesFromCommand(self,lastNode,command):
        nodes = []
        direction = command[0]
        if direction not in ('R','L','U','D'):
            print ( "Dirección no permitida")
            return null
        # Tenemos que meter esto en un try catch
        l = int(command[1:])
        x = lastNode.getX()
        y = lastNode.getY()

        if direction == 'R':
            for i in range(l):
                x += 1
                newNode = Point(x,y)
                nodes.append(newNode)
        if direction == 'L':
            for i in range(l):
                x -= 1
                newNode = Point(x,y)
                nodes.append(newNode)
        if direction == 'U':
            for i in range(l):
                y += 1
                newNode = Point(x,y)
                nodes.append(newNode)
        if direction == 'D':
            for i in range(l):
                y -= 1
                newNode = Point(x,y)
                nodes.append(newNode)
        return nodes

    def getNodes(self): 
        return self.nodes

    # Esta función mira si hay puntos en común entre dos paths
    def getCollisions(self,path):
        collisions = []
        nodes = path.getNodes()
        tam = len(self.nodes)
        i = 1
        j = 0
        for n in nodes: 
            print ("Trabajando: " + str(i) + "/" + str(tam) + " - Col: " + str(j))
            if n in self.nodes:
                collisions.append(n)
                j += 1
            i += 1
        return collisions

    def __str__(self) -> str:
        vstr = "<<"
        for node in self.nodes:
            vstr += node.__str__()
        vstr += ">>"
        return vstr
