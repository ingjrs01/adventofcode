class Point(): 

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def manhatan(self):
        return self.x + self.y

    def __eq__(self,p):
        if self.x == p.getX() and self.y == p.getY():
            return True

        return False

    def __str__(self) -> str:
        return ("(" + str(self.x) + "," + str(self.y) + ")")
