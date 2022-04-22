import sys

class Intcode():
    # return: Array de modos array[0] -> modo parámetro1, array[1] -> modo parámetro2,
    def get_mode_parameters(self,code):
        modes = [0,0,0]
        if code < 100:
            modes # Los dos primeros son operación
        tmp = code // 100

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


    def get_instruction(self,code)->int:
        if code == 99:
            return code

        if code < 10: 
            return code
        else:
            respuesta = code % 10

        return respuesta

    # Este método ejecuta una instrucción, y devuelve el puntero a la siguiente instrucción
    # ip = instruction pointer
    def execute_instruction(self,ip,instruction,modes,data,buffer):
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



    def run(self,data,buffer): 
        ip = 0 # Instruction point, Puntero que señala la posición de la siguiente instrucción

        while (ip < len(data)): 
            instruction = self.get_instruction(data[ip])
            modes = self.get_mode_parameters(data[ip])
            #print("***********************************************************************************************************")
            #print("Realizando instrucción en posición: " + str(ip))
            #print(instruction)
            #print(modes)
            #print(data)
            ip = self.execute_instruction(ip,instruction,modes,data,buffer)
            if ip == -1:
                break
    
        return data

    def process_file(self,filename):
        line = open(filename).readline()
        data =[int(x) for x in line.split(",")]
        return data


