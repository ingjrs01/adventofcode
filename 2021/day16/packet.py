class Packet():
    def __init__(self,version,ttype,literal):
        self.version = version
        self.type = ttype
        self.value = literal
        self.subpackets = []

    def appendSubpacket(self,packet):
        self.subpackets.append(packet)

    def __str__(self):
        tmp = "Version: " + str(self.version) + "\n"
        tmp += "Operación: " + str(self.type) + "\n"
        tmp += "Valor: " + str(self.value) + "\n"

        if (len(self.subpackets)>0):
            tmp += "-> Tiene Hijos\n"
            for p in self.subpackets:
                tmp += str(p)
        return tmp
