class Line:

    def __init__(self,p1,p2):
        if (p1[0] > p2[0]):
            self.p1 = p2
            self.p2 = p1
        elif (p1[0] == p2[0] and p1[1] > p2[1]):
            self.p1 = p2
            self.p2 = p1
        else:
            self.p1 = p1
            self.p2 = p2

        print(self.p1)
        print(self.p2)
        print(self.p2[0]-self.p1[0] )
        self.m = None
        if (self.p1[0] == self.p2[0]):
            self.m = None
        else:
            self.m = (self.p2[1]-self.p1[1])/(self.p2[0]-self.p1[0])
        if (self.m == 1):
            self.incremento = 1
        if (self.m == -1): 
            self.incremento = -1
        if(self.m == 0):
            self.incremento = 0
        if (self.m is None):
            self.incremento = 1

        #print("Pendiente: " + str(self.m) +  "  Incremento: " + str(self.incremento))
        # y = mx - b
        #ps = self.calc_points_i()
        #print(ps)
        #print("-----------------------------------------------------------------------")

    def calc_points_i(self):
        points = []
        points.append(self.p1)

        if (self.m is not None):
            y = self.p1[1]
            for i in range(self.p1[0]+1,self.p2[0]):
                y += self.incremento
                points.append((i,y)) 
        else:
            y = self.p1[1]
            for i in range(self.p1[1]+1,self.p2[1]):
                y += self.incremento
                points.append((self.p1[0],y))
        points.append(self.p2)
        return (points)

    def calc_points(self):
        points = []
        points.append(self.p1)
        points.append(self.p2)
        if (self.p1[0] == self.p2[0]):
            if (self.p1[1] > self.p2[1]):
                begin = self.p2[1]+1
                end = self.p1[1]
            else:
                begin = self.p1[1]+1
                end = self.p2[1]

            for i in range(begin,end):
                points.append((self.p1[0],i))

        elif (self.p1[1] == self.p2[1]):
            if (self.p1[0] > self.p2[0]):
                begin = self.p2[0]+1
                end = self.p1[0]
            else:
                begin = self.p1[0]+1
                end = self.p2[0]
            for i in range(begin,end):
                points.append((i,self.p1[1]))
        else:
            return []
        
        return (points)
