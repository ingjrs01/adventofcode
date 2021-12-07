class Machine():

    def __init__(self):
        self.pointer = 0
        self.accum = 0
        self.visited = []
    
    def run(self,program):
        salir = False
        while (salir == False):
            if (self.pointer in self.visited):
                return False

            if (self.pointer >= len(program)):
                return True

            self.visited.append(self.pointer)
            incremento = 1 

            if (program[self.pointer][0] == "acc"):
                self.accum += program[self.pointer][1]
            
            if (program[self.pointer][0] == "jmp"):
                incremento = program[self.pointer][1]
            
            self.pointer += incremento

        
        return True

    def getVisited(self):
        return self.visited

    def getAccum(self):
        return self.accum

    
