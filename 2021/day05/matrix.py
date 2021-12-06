from line import Line 

class Matrix:

    def __init__(self):
        self.width = 1000
        self.height = 1000
        self.data = []

        for i in range(self.width):
            row = []
            for j in range(self.height):
                row.append(0)
            self.data.append(row)
    
    def __str__(self) -> str:
        s = ""
        for i in range(self.width):
            for j in range(self.height):
                s += str(self.data[i][j] ) + ", "
            s += "\n"
        return s

    def add_line(self,line):
        points = line.calc_points_i()
        for point in points:
            self.data[point[0]][point[1]] += 1

    def get_num_inter(self):
        count = 0
        for i in range(self.width):
            for j in range(self.height):
                if self.data[i][j] > 1:
                    count += 1
        return count

