class Line:

    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        self.calc_points()

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
