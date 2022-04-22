


A tu máquina Intcode  le falta una funcionalidad, son los parámetros en modo relativo. 

Parámetros en modo 2. Son muy similares a los parámetros en modo posición, pero no se empieza a contar en la posición cero, se cuenta desde una posición x

Esa posición x comienza siendo la posición 0, pero una nueva orden puede cambiar el valor de esa X. 

op 9 -> ajusta la posición relativa. Le pasamos un parámetro, que será el número de posiciones que avanzará hacia adelante o hacía detrás