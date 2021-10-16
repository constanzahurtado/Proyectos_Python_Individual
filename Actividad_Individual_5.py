#Desarrollo Actividad Individual 5

# Familiarizado ya con estos componentes debemos prepararnos para realizar las siguientes acciones, para simular el 
# funcionamiento de tu aplicación.

# El desafío de hoy consiste en crear un registro de 10 usuarios de su aplicación. Los usuarios se pueden registrar por 
# la terminal, hasta que quien registra indique el concepto clave ‘Salida’.

# Deberán disponer la edad y el nombre de cada usuario. Esta información debe ser guardada en un tipo de dato que 
# consideres pertinente para el registro.

# El siguiente aspecto a desarrollar, consiste en imprimir cinco nombres con sus respectivas edades, de forma ordenada y 
# con un formato interesante. Todo esto dentro de los elementos visuales que nos proporciona la terminal. Luego debe 
# mostrar cinco usuarios más, si es que se ingresa ‘Más usuarios’ por terminal.

# El producto de este trabajo deben publicarlo en sus repositorios github.

import time
import random

usuario = 1 #Variable contador para ciclo while
diccionarioUsuarios = {} #Variable diccionario para almacenar datos

#Se crea un ciclo while que se ejecutará hasta que el número de usuarios se mayor a 10
while usuario <=10:
    nombre = input('Ingrese su nombre: ') #Se ingresa el nombre del usuario
    edad = str(input('Ingrese su edad: ')) #Se ingresa la edad del usuario
    diccionarioUsuarios[nombre] = edad #Almacenamos los datos en un diccionario
    usuario += 1 #aumentamos el contador

print('Estos son nuestros primeros usuarios')

#Este ciclo for permite imprimir los primeros 5 usuarios del diccionario. Se aplica la función format. 
for x in list(diccionarioUsuarios)[0:5]:
    print ("{}, {} ".format(x, diccionarioUsuarios[x]))

#Si se desea ver el resto de usuarios, se aplica el mismo ciclo for, pero con la función reverse. 
respuesta = input('Para ver el resto de usuarios, ingrese ‘Más usuarios’: ')

if respuesta == 'Más usuarios':
    for x in list(reversed(diccionarioUsuarios))[0:5]:
        print ("{}, {} ".format(x, diccionarioUsuarios[x]))




