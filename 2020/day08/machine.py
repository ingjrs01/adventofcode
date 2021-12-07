class Machine():

    def __init__(self,lines):
        print("Iniciando la máquina")
        self.accum = 0
        self.original = []
        self.program = []
        self.pointer = 0
        self.visited = []
        for line in lines: 
            l = line.rstrip()
            parts = l.split(" ")
            value = int(parts[1])
            self.program.append((parts[0],value))
            self.original.append((parts[0],value))
            #print(l)
        print(self.program)


    def run(self,program):
        print("La máquina hecha a andar")
        finish = False
        #for i in self.program:        
        self.pointer = 0
        self.visited = []
        while (not finish):
            if (self.pointer > len(program)):
                # El programa finaliza correctamente
                print("Acumulador: " + str(self.accum) )
                return  True

            i = program[self.pointer]
            print("Instrucción: ",end='')
            print(i,end='')
            print("   puntero: " + str(self.pointer))
            #print("Ejecutando instrucción número: " + str(self.pointer))
            if self.pointer in self.visited:
                print("Saliendo")
                print(self.pointer)
                print(self.visited)
                print("Estos fueron los visitados")
                print(self.accum)
                finish = True
                return False
            else: 
                self.visited.append(self.pointer)
                print(i)
                if (i[0] == "acc"):
                    self.acc(int(i[1]))
                if (i[0] == "jmp"):
                    self.jmp(int(i[1]))
                if (i[0] == "nop"):
                    self.nop(int(i[1]))
        #print("Resultado: " + str(self.accum))
        return self.accum

    def acc(self,value):
        #print("Estoy haciendo acc")
        self.accum += value
        self.pointer += 1
    
    def jmp(self,value):
        print("Estoy haciendo jmp")
        self.pointer += value
    
    def nop(self,value):
        #print("Estoy haciendo nop")
        self.pointer += 1

    def run2(self):
        print("segunda parte")        
        #self.program[419] = ('nop',1)
        for index in range(len(self.program)): 
            if (self.program[index][0] == 'jmp'):
                copia = self.program
                copia[index] = ('nop',copia[index][1])
                res = self.run(copia)
                if (res ): 
                    print("Hemos encontrado")
                    print(res)
                    return True


    def __str__(self):
        print(self.acc)

