def dosiguales(d1,d2,d3,d4,d5,d6):
    if d1 == d2:
        return True
    if d2 == d3:
        return True
    if d3 == d4: 
        return True
    if d4 == d5:
        return True
    if d5 == d6:
        return True
    return False

d1 = 1
d2 = 3
d3 = 4
d4 = 5
d5 = 6
d6 = 5
contador = 0
salir = False
numero = 0
#J = 0 
while not salir:
#    J = J + 1
#    if J > 300:
#        salir = True

    print ("salir " + str(d1) + "-" + str(d2) + "-" + str(d3)+ "-"+ str(d4)+ "-"+ str(d5)+ "-" + str(d6))
    if numero > 585159:
        salir = True

    d6 += 1
    if d6 > 9:
        d5 += 1
        d6 = d5
    if d5 > 9:
        d4 += 1
        d5 = d4
        d6 = d5 + 1
        if d6 > 9:
            d4 += 1
    if d4 > 9:
        d3 += 1
        d4 = d3
        d5 = d3 + 1 
        d6 = d5
        if d5 > 9:
            d3 += 1

    if d3 > 9:
        d2 += 1
        d3 = d2
        d4 = d2 + 1 
        d5 = d4 
        d6 = d5 + 1
        if d4 > 9:
            d2 += 1
        if d6 > 9: 
            d2 += 2

    if d2 > 9:
        d1 += 1
        d2 = d1
        d3 = d1 + 1
        d4 = d3
        d5 = d4 + 1
        d6 = d5
    
    if dosiguales(d1,d2,d3,d4,d5,d6):
        numero = d6 + d5 * 10 + d4 * 100 + d3 * 1000 + d2 * 10000 + d1 * 100000
        if numero > 585159:
            salir = True
        else:
            print(numero)
            contador += 1
    
print("Hay " + str(contador) + " opciones")
