from point import Point
from path import Path
import sys

#print ("Working...")
s1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
s2 = "R2,U3,R1"
f = open('input')
s1 = f.readline()
s2 = f.readline()
print(s1)
print(s2)

path1 = Path(s1)
path2 = Path(s2)
#print(path1)
#print("...........")
#print(path2)
print("Obteniendo colisiones")
points = path1.getCollisions(path2)
print("Todas las colisiones obtenidas")

dis_min = 9999999
for point in points: 
    print(point)
    distancia = point.manhatan()
    print("Distancia Manhatan: " + str(distancia))
    if distancia < dis_min:
        dis_min = distancia

print("La distancia mínima es: " + dis_min)

#print (points)


#for point in points:
#    print (point)

#a = Point(3,3)
#b = Point(12,4)
#
#print (a)
#print (b)
#print ("Distancia Manhatan " + str(a.manhatan()))
#print ("Distancia Manhatan " + str(b.manhatan()))
#print ("Fin")
