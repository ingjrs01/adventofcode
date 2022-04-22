# Tiene que resolver el problema de Calcular el fuel

import sys

def calculate_fuel(mass):
    return int(mass / 3) - 2

filename = 'input'
if (len(sys.argv) > 1):
    filename = str(sys.argv[1])

Lines = open(filename).readlines()
masses = [int (x) for x in Lines]

total_fuel = 0
for mass in masses:
    fuel = calculate_fuel(mass)
    total_fuel += fuel
    print ("Masa: " + str(mass) + " Fuel " + str(fuel))
    while (fuel > 8): 
        fuel = calculate_fuel(fuel)
        print ("     => " + str(fuel))
        total_fuel += fuel


#fuels = [int(x / 3) - 2 for x in masses]
print ("Fuel total: " + str(total_fuel))

