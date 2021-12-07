from machine import Machine

lines = [line.strip() for line in open('input2','r').readlines()]
program = []
for line in lines:
    p2 = line.split()
    program.append([p2[0].strip(),int(p2[1])])

#print(program)
machine = Machine()
machine.run(program)

visitados = machine.getVisited()

anterior = ""
program2 = list( program)
for i in visitados: 
    anterior = program2[i][0]
    if (program2[i][0] == "nop"):
        program2[i][0] = "jmp"
        machine2 = Machine()
        if (machine2.run(program2)):
            print("Acumulado : " + str(machine2.getAccum()))
            exit(0)
        program2[i][0] = anterior
    
    if (program2[i][0] == "jmp"):
        program2[i][0] = "nop"
        machine2 = Machine()
        if (machine2.run(program2)):
            print("Acumulado : " + str(machine2.getAccum()))
            exit(0)
        program2[i][0] = anterior