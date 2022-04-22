#from point import Point
from sympy import Point, Line, Segment
from path2 import Path
import sys
import sympy as sym


def probar_cruces():
    p1 = Point(0,1)
    p2 = Point(4,1)

    p3 = Point(2,3)
    p4 = Point(2,8)

    s1 = Segment(p1,p2)
    s2 = Segment(p3,p4)

    r = s1.intersection(s2)
    print(r)

def get_segments(path):
    nodes = path.getNodes()

    tam = len(nodes)
    segments = []
    for i in range(1,tam):
        x1,y1 = nodes[i-1]
        x2,y2 = nodes[i]
        segments.append(Segment(Point(x1,y1),Point(x2,y2)))
    
    return segments

s1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
s2 = "U62,R66,U55,R34,D71,R55,D58,R83"
s1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
s2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
f = open('input')
s1 = f.readline()
s2 = f.readline()
print(s1)
print(s2)

path1 = Path(s1)
path2 = Path(s2)
print(path1)
print(path2)
segments1 = get_segments(path1)
segments2 = get_segments(path2)

collisions = []
i = 0
j = 0
for seg in  segments1:    
    for seg2 in segments2:     
        collision = seg.intersection(seg2)
        j += 1
        #print ("i : " + str(i) + " j : " + str(j))
        if len(collision) > 0:
            for c in collision:
                print(c)
                # Los segmentos implicados son seg y seg2
                # Tenemos que calcular la distancia
                # d1 = distancia a la colisión del trayecto 1
                d1 = 0
                print("-> Colisión")
                print(seg)
                print(seg2)
                for n in range(0,i):
                    d1 += abs(segments1[n].length)
                    print("Tamaño segmento: i" + str(i) + " n: " + str(n) + " j:" + str(j) + "  " + str(segments1[n].length))
                tmp1,tmp2 = seg.points
                smp1 = Segment(tmp1,c)
                d1 += abs(smp1.length)
                print("  ultimo segmento: " + str(smp1.length))
                print ("Tamaño p1: " + str(d1))

                print("                     -----        ")
                d2 = 0
                for n in range(0,j-1):
                    d2 += abs(segments2[n].length)
                    print("Tamaño segmento: " + str(n) + " j:" + str(j) + "  " + str(segments2[n].length))
                tmp1,tmp2 = seg2.points
                smp1 = Segment(tmp1,c)
                d2 += abs(smp1.length)
                print ("   ultimo segmento: " + str(smp1.length))
                print ("Tamaño p2: " + str(d2))
                collisions.append((c,d1,d2))
            print("          ***********************************************")
    i += 1
    j = 0
print (collisions)
print("------------------------------------------------------------")
#node = collisions[2]
#manhatan = abs(node.x) + abs(node.y)
#print("X = " + str(node.x) + " Y = " + str(node.y) + "  distancia = " + str(manhatan))
print("------------------------------------------------------------")
for x in collisions:
    a,b,c = x
    print ("Punto ",end='')
    print(a,end='')
    print("  suma = " + str(b+c))








