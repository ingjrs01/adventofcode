class Carton:
    
    def __init__(self,numbers):
        self.tam = 5
        self.data = []
        for i in range(self.tam):
            linea = []
            for j in range(self.tam):
                linea.append([numbers[i][j],0])
            self.data.append(linea)

    def __str__(self):
        s = ""
        for i in range(self.tam):
            for j in range(self.tam):
                s += str(self.data[i][j][0]) + "-> " +  str(self.data[i][j][1]) + ", "
            s += "\n"

        s += "SUMA: " + str(self.sum_unmarked())
        return (s)

    def sum_unmarked(self):
        s = 0

        for i in range(self.tam):
            for j in range(self.tam):
                if (self.data[i][j][1] == 0):
                    s+= self.data[i][j][0]
        return (s)
    
    def mark(self,num):
        for i in range(self.tam):
            for j in range(self.tam):
                if (self.data[i][j][0] == num):
                    self.data[i][j][1] = 1
                    return True
        return False
    
    def check(self):
        for i in range(self.tam):
            s = 0
            for j in range(self.tam):
                s += self.data[i][j][1]

            if (s == 5):
                return True # Hay línea
        
        for i in range(self.tam):
            s = 0
            for j in range(self.tam):
                s += self.data[j][i][1]

            if (s == 5):
                return True # Hay  columna
        return False


    def imprimir(self):
        for i in range(self.tam):
            for j in range(self.tam):
                print (self.data[i][j]) 