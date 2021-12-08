
lines = open('input','r')

tam = [2,3,4,7]
total = 0
for line in lines:
    #print (line)
    words = line.split("|")[1].split()
    print(words)
    for w in words:

        if (len(w) in tam):
            print(w) 
            total += 1

print(total)


se reconocer 1,4, 7 y 8

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf


    acedgfb: 8
    cdfbe: 5
    gcdfa: 2
    fbcad: 3
    dab: 7     d -> a  a -> c  b -> f
    cefabd: 9
    cdfgeb: 6
    eafb: 4      e -> b , f -> d
    cagedb: 0
    ab: 1     a -> c   b -> f

Then, the four digits of the output value can be decoded:

    cdfeb: 5
    fcadb: 3
    cdfeb: 5
    cdbaf: 3
