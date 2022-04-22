import re

class Passport: 
    
        def __init__(self):
            self.byr = None  # (Birth Year)
            self.iyr = None  # (Issue Year)
            self.eyr = None  # (Expiration Year)
            self.hgt = None  # (Height)
            self.hcl = None  # (Hair Color)
            self.ecl = None  # (Eye Color)
            self.pid = None  # (Passport ID)
            self.cid = None  # (Country ID)

        def is_valid_height(self,value):
            units = value[-2:]
            if units not in ["in","cm"]:
                return False
            val = int(value[:-2])
            if ( (units == "cm") and (val >= 150) and (val <= 193)):
                return True
            if ( (units == "in") and (val >= 59) and (val <= 76)):
                return True

            return False


        def is_valid(self):
            if ((self.byr == None) or (self.byr < 1920) or (self.byr > 2002)): 
                return False
            if ((self.iyr == None) or (self.iyr < 2010) or (self.iyr > 2020)): 
                return False
            if ((self.eyr == None)  or (self.eyr < 2020) or (self.eyr > 2030)): 
                return False
            if ((self.hgt == None) or (self.is_valid_height(self.hgt) == False)): 
                return False
            if ((self.hcl == None) or re.search("#([a-f]|[A-F]|[0-9]){6}",self.hcl)== None): 
                return False
            if ((self.ecl == None) or (self.ecl not in ["amb","blu","brn","gry","grn","hzl","oth"])): 
                return False
            if ((self.pid == None) or (re.search("([0-9]){9}",self.pid)== None)): 
                return False

            return True
            
        def __str__(self):
            sstr =  "byr: " + str(self.byr) + "\n"
            sstr += "iyr: " + str(self.iyr) + "\n"
            sstr += "eyr: " + str(self.eyr) + "\n"
            sstr += "hgt: " + str(self.hgt) + "\n"
            sstr += "hcl: " + str(self.hcl) + "\n"
            sstr += "ecl: " + str(self.ecl) + "\n"
            sstr += "pid: " + str(self.pid) + "\n"
            sstr += "cid: " + str(self.cid) + "\n"

            return sstr

def analize_line(line,obj):
    pares = line.rstrip().split(" ")
    for par in pares:
        key,value = par.split(":")
        #print("Clave : " + key + "  Valor " + str(value))
        if ("byr" == key):
            obj.byr = int(value)
        if ("iyr" == key):
            obj.iyr = int(value)
        if ("eyr" == key):
            obj.eyr = int(value)
        if ("hgt" == key):
            obj.hgt = value            
        if ("hcl" == key):
            obj.hcl = value
        if ("ecl" == key):
            obj.ecl = value
        if ("pid" == key):
            obj.pid = value
        if ("cid" == key):
            obj.cid = value
    
    
def process_file(filename):
    lines = open(filename).readlines()
    cont = 0
    passports = []
    tmp = Passport()
    for line in lines: 
        if (line == "\n"):
            if (tmp.is_valid()):
                cont += 1
                print("Válido: " + str(cont) + "\n" + str(tmp))
            #else:
            #    print("No válido" + str(tmp))
            passports.append(tmp)
            tmp = Passport()
        else:
            analize_line(line,tmp)
            #print(tmp)
    #print("Último elemento")
    #print(passports[len(passports)-1])
    #print("Elemento actual")
    #print(tmp)
    if (tmp.is_valid()):
        cont += 1
        print("Válido: " + str(cont) + "\n" + str(tmp))
    
    print ("Tenemos " + str(cont))

process_file("input.txt")
