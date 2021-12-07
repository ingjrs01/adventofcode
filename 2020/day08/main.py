from machine import Machine

def read_file(filename):
    lines = open(filename).readlines()
    print(lines)
    machine = Machine(lines)
    res = machine.run2()
    print("Acumulador: " + str(res))

read_file("input2")
