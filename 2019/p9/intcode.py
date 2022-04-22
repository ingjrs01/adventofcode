import sys

class Intcode():
    # Constructor de la clase
    def __init__(self):
        self.instruction_pointer = 0  # Apunta a la instrucción que hay que ejecutar
        self.data                = [] # Simula el algoritmo Intcode
        self.relative_point      = 0  # Punto relativo para 
        self.buffer              = [] # Buffer de entrada y salida de datos
        self.instructions = {}
        self.instructions[1] = {'method':'sum','params':3}
        self.instructions[2] = {'method':'product','params':3}
        self.instructions[3] = {'method':'input','params':1}
        self.instructions[4] = {'method':'output','params':1}
        self.instructions[5] = {'method':'different','params':2}
        self.instructions[6] = {'method':'iszero','params':2}
        self.instructions[7] = {'method':'lessthan','params':3}
        self.instructions[8] = {'method':'equal','params':3}
        self.instructions[99] = {'method':'exit','params':0}

    def exit(self):
        print("Saliendo del programa")

    def prueba(self):
        m = globals()['Intcode']()
        method = getattr(m,self.instructions[99]['method'])
        method()

    def set_data(self,data): 
        self.data = data
        self.instruction_pointer = 0

    # return: Array de modos array[0] -> modo parámetro1, array[1] -> modo parámetro2,
    def get_mode_parameters(self):
        code = self.data[self.instruction_pointer]
        modes = [0,0,0]
        if code < 100:
            return modes

        tmp = code // 100 # División entera

        if tmp < 10:
            modes[0] = tmp
        else: 
            i = 0
            while tmp > 0:
                resto = tmp % 10
                cociente = tmp // 10
                modes[i] = resto
                tmp = cociente
                i += 1

        return modes


    def get_instruction(self)->int:
        code = self.data[self.instruction_pointer]
        if code == 99:
            return code

        if code < 10: 
            return code
        else:
            respuesta = code % 10

        return respuesta

    # Devuelve un array de parámetros, para realizar la operación que sea necesaria. 
    def get_parameters(self,instruction,modes):
        #code = self.data[self.instruction_pointer]
        n = self.instructions[instruction]['params']-1
        parameters = []
        for i in range(0,n):
            if modes[i] == 0: 
                parameters.append(self.data[self.data[self.instruction_pointer + i+1]])
            if modes[i] == 1:
                parameters.append(self.data[self.instruction_pointer + i + 1])
            if modes[i] == 2:
                parameters.append(self.data[self.relative_point + self.data[self.instruction_pointer + i + 1]])
        parameters.append(self.data[n+1])

        return parameters


    # Este método ejecuta una instrucción, y devuelve el puntero a la siguiente instrucción
    def execute_instruction(self,instruction,modes,data,buffer):
        if instruction in [1,2,5,6,7,8]: 
            # Todas estas instrucciones tienen dos parámetros
            if modes[0] == 0:
                op1 = data[data[ip + 1]]
            else:
                op1 = data[ip + 1]

            if modes[1] == 0:
                op2 = data[data[ip + 2]]
            else:
                op2 = data[ip + 2]
        if instruction == 4:
            if modes[0] == 0:
                op1 = data[data[ip+1]]
            else:
                op1 = data[ip+1]

        if (instruction == 99): 
            ip = -1
            return ip

        if (instruction == 1):
            data[data[ip + 3]] = op1 + op2
            ip += 4

        if (instruction == 2):
            data[data[ip + 3]] = op1 * op2
            ip += 4
        
        if (instruction == 3): 
            #r = input("Valor a introducir: ")
            dato = buffer.pop(0)
            #print("Pide dato, le doy un: " + str(dato))
            data[data[ip + 1]] = dato
            ip += 2

        if (instruction == 4): 
            #print("Mostrando el valor: " + str(op1))
            buffer.append(op1)
            ip += 2
        
        if (instruction == 5): 
            if op1 != 0:
                ip = op2
            else: 
                ip += 3 # 

        if (instruction == 6): 
            if op1 == 0:
                ip = op2
            else: 
                ip += 3 # 

        if (instruction == 7):
            if op1 < op2:
                data[data[ip + 3]] = 1
            else:
                data[data[ip + 3]] = 0            
            ip += 4

        if (instruction == 8):
            if op1 == op2:
                data[data[ip + 3]] = 1
            else:
                data[data[ip + 3]] = 0            
            ip += 4
        # Otras instrucciones

        if (instruction > 8):
            print("Instrucción incorrecta en " + str(ip))
            print(data)
        return ip

    def sum(self,parameters): 
        self.data[parameters[2]] = parameters[0] + parameters[1]
        self.instruction_pointer += self.instructions[1]['params'] + 1

    def product(self,parameters):
        self.data[parameters[2]] = parameters[0] * parameters[1]
        self.instruction_pointer += self.instructions[2]['params'] + 1

    def input(self,parameters):
        self.data[self.data[self.instruction_pointer + 1]] = self.buffer.pop(0)
        self.instruction_pointer += self.instructions[3]['params']+1

    # Se ejecuta el algoritmo para los datos cargados. 
    def run(self, buffer): 
        #m = globals()['Intcode']()
        #print(m)
        
        while (self.instruction_pointer < len(self.data)): 
            instruction = self.get_instruction() #(data[ip])
            modes = self.get_mode_parameters()   #(data[ip])
            parameters = self.get_parameters(instruction,modes)
            #self.execute_instruction(instruction,modes,buffer)
            method = getattr(self,self.instructions[instruction]['method'])
            method(parameters)
            print("ando en bucle " + str(self.instruction_pointer) + "  tamaño: " + str(len(self.data)))

            if self.instruction_pointer == -1:
                break
    
        return self.data

    def process_file(self,filename):
        line = open(filename).readline()
        self.data =[int(x) for x in line.split(",")]
        #return data
    
    def get_intcode():
        return self.data


