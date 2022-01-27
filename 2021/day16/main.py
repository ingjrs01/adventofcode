from packet import Packet

def hex2bin(t):
    d = {}
    d['0'] = '0000'
    d['1'] = '0001'
    d['2'] = '0010'
    d['3'] = '0011'
    d['4'] = '0100'
    d['5'] = '0101'
    d['6'] = '0110'
    d['7'] = '0111'
    d['8'] = '1000'
    d['9'] = '1001'
    d['A'] = '1010'
    d['B'] = '1011'
    d['C'] = '1100'
    d['D'] = '1101'
    d['E'] = '1110'
    d['F'] = '1111'
    cadena = ""
    for c in t:
        cadena += d[c]

    return (cadena)

def read_file(filename):
    return (open(filename,'r').readline().strip())

# l_bits indicates the number of bits that have trate this packet
def proccess_str(t,l_bits,npackets):
    print("llegando a process")
    packets = []
    salir = False
    i = 0
    procesado = 0
    while (salir == False) :
        version = int(t[i:i+3],2)
        tipe = int(t[i+3:i+6],2)
        value = ""
        subpackets = []
        if (tipe == 4):
            print("Es un literal")
            value_bin = read_literal(t[i+6:])
            value= int (value_bin,2)
            p = Packet(version,tipe,value)
            packets.append(p)
            procesado += len(value_bin) + len(value_bin) // 4 + 6
            print(f"Probando {procesado} y {l_bits} i = {i} -> {value_bin}")
            if (procesado >= l_bits): 
                print("saliendo")
                salir = True
            i += procesado 
        else:
            print("Es un operador")
            if (t[6] == '0'):
                # leo 15 bits siguientes
                lenght_bits = int(t[7:22],2)
                print("Tamaño en bits: " + str(lenght_bits))
                print("Procesar str: " + t[22:22+lenght_bits])
                p = Packet(version,tipe,0)

                subpackets = proccess_str(t[22:22+lenght_bits],lenght_bits)
                for s in subpackets:
                    p.appendSubpacket(s)

                packets.append(p)
                # Tener cuidado con lo que vamos a procesar
            else:
                # leo 11 bits siguientes
                lenght_bits = int(t[7:18],2)
            salir = True
        print("punto de salida")

    return packets

def read_literal(t):
    # Leo los caracteres de 5 en 5
    i = -5
    flag = True
    tmp = ""
    while (flag):
        i += 5
        tmp += t[i+1:i+5]
        if (t[i] == '0'):
            flag = False
    return (tmp)


def proccess_package(t):
    p = Packet(t)
    return p



#t= '620080001611562C8802118E34'
t = '38006F45291200'
#t2 = hex2bin(read_file('input'))
t2 = hex2bin(t)
print("Cadena total a procesar: ",end='')
print(t2)

ps = proccess_str(t2,0,0)
print("Hora de imprimir")
for p in ps:
    print(p)

