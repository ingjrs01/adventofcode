from intcode import Intcode
import sys

print("Incode 5 is running...")
filename='input'
if (len(sys.argv) > 1):
    filename = str(sys.argv[1])

machine = Intcode()

datos = machine.process_file(filename)
print(datos)

#datos = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

machine.run(datos)