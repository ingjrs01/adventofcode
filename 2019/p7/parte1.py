from intcode import Intcode
import sys
import itertools

print("Incode 7 is running...")
filename='input'
if (len(sys.argv) > 1):
    filename = str(sys.argv[1])

combinaciones =list(itertools.permutations([0,1,2,3,4]))
#print(combinaciones)
#print("Tamaño: " + str(len(combinaciones)))
#exit(0)

machine = Intcode()
datos = machine.process_file(filename)
#datos = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]

buffer = []
#buffer.append(0) # Este dato me lo da el programa porque si
actual_signal = 0
best_signal = 0
combination_id = []

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#phases = [0,1,2,3,4]
#print ("::: Combinación: ",end='')
#print (phases,end='')
#buffer.append(0)
#for i in phases:
#    print ("Entrando en amplificador - ---------------------------------------------------------")
#    buffer.insert(0,i)
#    print("Buffer: ",end='')
#    print(buffer)
#
#    machine.run(datos.copy(),buffer)
#    #buffer.insert(0,phases[1])
#actual_signal = buffer.pop()
#print("  señal enviada: " + str(actual_signal))
#
#
#exit(0)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

for phases in combinaciones:
    #print ("::: Combinación: ",end='')
    #print (phases,end='')
    buffer.append(0)
    for i in phases:
        #print ("Entrando en amplificador - ---------------------------------------------------------")
        buffer.insert(0,i)
        #print("Buffer: ",end='')
        #print(buffer)

        machine.run(datos.copy(),buffer)
        #buffer.insert(0,phases[1])
    actual_signal = buffer.pop()
    print("  señal enviada: " + str(actual_signal))
    if actual_signal > best_signal:
        combination_id = phases
        best_signal = actual_signal

print("Mejor combinación: ",end='')
print(combination_id)
print("Mejor señal: " + str(best_signal))