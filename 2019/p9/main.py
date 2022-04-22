from intcode import Intcode
import sys
import itertools

print("Incode 9 is running...")
filename='input'
if (len(sys.argv) > 1):
    filename = str(sys.argv[1])

machine = Intcode()
machine.prueba()
#datos = machine.process_file(filename)
#print(datos)