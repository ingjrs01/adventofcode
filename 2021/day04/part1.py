from carton import Carton

f = open('input','r')

entry = [int(s) for s in f.readline().split(",")]

lines = f.readlines()
t = len(lines)

i = 1
cards = []
while (i < t):
    data = []
    for j in range(5):
        data.append([int(v) for v in lines[i].split()])
        i += 1
    d = Carton(data)
    cards.append(d)
    i += 1 ## Una linéa en blanco

for n in entry:
    if (len(cards) == 0):
        exit(0)
    print("Probando el número: " + str(n))
    borrados = []
    for card in cards:
        card.mark(n)
        if (card.check()):
            print("Hemos encontrado línea")
            print(card)
            print("Numero: " + str(n))
            print(card.sum_unmarked() * n)
            borrados.append(card)
            #print("Número de tarjetas " + str(len(cards)))
            #exit(0)
        else:
            print(card)
    print("_______________________________________________________________________________________") 
    for b in borrados:
        cards.remove(b)
