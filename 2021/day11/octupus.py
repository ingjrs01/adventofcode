class Octopus():

    def __init__(self,val,x,y):
        self.val = val
        self.x = x
        self.y = y
        self.flashes = 0
        self.neighbors = []
    
    def getVal(self):
        return self.val
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def step(self):
        self.flashes = 0
        self.add()
    
    def add(self):
        if (self.flashes ==0):
            self.val += 1

    def autoinc(self):
        if (self.flashes ==0):
            self.val += 1
        self.check()

    def check(self):
        if (self.val > 9 and self.flashes == 0):
            self.flash()

    def flash(self):
        self.flashes += 1
        for neighbord in self.neighbors:
            i = neighbord.getX()
            j = neighbord.getY()
            #print(f"Imprimiendo ({i},{j}")
            neighbord.autoinc()
        self.val = 0
        return True
    
    def getNeighbors(self):
        positions = []
        if (self.x > 0):
            if (self.y > 0):
                positions.append((self.x-1,self.y-1))
            positions.append((self.x-1,self.y))
            if (self.y < 9):
                positions.append((self.x-1,self.y+1))
        if (self.y > 0):
            positions.append((self.x,self.y-1))
        if (self.y < 9):
            positions.append((self.x,self.y+1))
        if (self.x < 9):
            if (self.y >0):
                positions.append((self.x+1,self.y-1))
            positions.append((self.x+1,self.y))
            if (self.y < 9):
                positions.append((self.x+1,self.y+1))
        return positions
    
    def setNeighbors(self,neighbors):
        self.neighbors = neighbors
