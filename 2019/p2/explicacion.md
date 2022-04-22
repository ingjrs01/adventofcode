
Tenemos que construír ua intcode program: 

Un Incode program es una lista de enteros separados por comas, como por ejemplo: 
1,0,0,3,99

Al primer dígito lo llamamos opcode, e identifica la operación a realizar: 
1  -> Indica que la operación a realizar es una suma
2  -> Indica que la operación a realizar es una multiplicación
99 -> El programa finaliza.

Cualquier otro código se considera un error. 

Si la operación no es 99, para realizar la operación tenemos los siguientes 3 valores. Los dos 
primeros son las direcciones de los datos de entrada, y el tercero es la dirección del dato de salida.

Una vez procesado un opcode, nos movemos hacia adelante 4 posiciones. 



-----------------------------------
Terminología. 

A la lista inicial de datos, la llamaremos estado inicial de la memoria. 
Cada posición en esa memoria la llamamos "address". 

El primer dígito es opcode, como ya vimos, y los 3 siguientes, son los parámetros. 
La dirección de la instrucción actual, es "

