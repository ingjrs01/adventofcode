--- Day 6: Chronal Coordinates ---

El dispositivo en su muñeca emite un pitido varias veces, y una vez más siente que se está cayendo.

" Situación crítica ", anuncia el dispositivo. "Destino indeterminado. Se ha detectado una interferencia crónica. Especifique nuevas coordenadas del objetivo".

Luego, el dispositivo produce una lista de coordenadas (su entrada de rompecabezas). ¿Son lugares que cree que son seguros o peligrosos? Le recomienda que consulte el manual de la página 729. Los Elfos no le dieron un manual.

Si son peligrosos, tal vez pueda minimizar el peligro al encontrar la coordenada que proporciona la mayor distancia desde los otros puntos.

Usando solo la distancia de Manhattan , determine el área alrededor de cada coordenada contando el número de ubicaciones enteras X, Y que están más cercanas a esa coordenada (y no están vinculadas en la distancia a ninguna otra coordenada).

Su objetivo es encontrar el tamaño del área más grande que no sea infinita. Por ejemplo, considere la siguiente lista de coordenadas: 

1, 1
1, 6
8, 3
3, 4
5, 5
8, 9


Si nombramos estas coordenadas de la A a la F , podemos dibujarlas en una cuadrícula, colocando 0,0 en la 0,0 superior izquierda:
..........
.A........
..........
........C.
...D......
.....E....
.B........
..........
..........
........F.

 Esta vista es parcial: la cuadrícula real se extiende infinitamente en todas las direcciones. Usando la distancia de Manhattan, se puede determinar la coordenada más cercana de cada ubicación, que se muestra aquí en minúsculas: 

aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf

Las ubicaciones se muestran como . están igualmente lejos de dos o más coordenadas, por lo que no cuentan como las más cercanas a ninguna.

En este ejemplo, las áreas de coordenadas A, B, C y F son infinitas, aunque no se muestran aquí, sus áreas se extienden para siempre fuera de la cuadrícula visible. Sin embargo, las áreas de coordenadas D y E son finitas: D está más cerca de 9 ubicaciones y E está más cerca de 17 (ambas incluyendo la ubicación de la coordenada en sí). Por lo tanto, en este ejemplo, el tamaño del área más grande es 17 .

¿Cuál es el tamaño del área más grande que no es infinita? 

Locations shown as . are equally far from two or more coordinates, and so they don't count as being closest to any.

In this example, the areas of coordinates A, B, C, and F are infinite - while not shown here, their areas extend forever outside the visible grid. However, the areas of coordinates D and E are finite: D is closest to 9 locations, and E is closest to 17 (both including the coordinate's location itself). Therefore, in this example, the size of the largest area is 17.

What is the size of the largest area that isn't infinite?

To begin, get your puzzle input.

Answer:

You can also [Shareon Twitter Mastodon] this puzzle.
