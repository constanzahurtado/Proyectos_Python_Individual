# •	Esta aplicación debe entregar la posibilidad de iniciar sesión con un perfil individual.
# •	Generalmente, uno ingresa a su cuenta personal en una página, ésta te saluda y te reconoce


#Intentemos replicar esto. Crea un string con el nombre de al menos 7 usuarios de tu aplicación.
#Se crea una variable String que contiene 7 nombres. 

usuarios = 'Sofía,Luís,Antonio,Juan,Sandra,Estéban,Lucía'
print(usuarios)

# •	Ahora piensa en tres de ellos. Búscalos en la lista con el método adecuado.
#Se utiliza la fución find() para encontrar el índice de tres usuarios

print(usuarios.find('Antonio'))
print(usuarios.find('Luís'))
print(usuarios.find('Sofía'))

# •	Convierte tu string en una lista, en la cual cada elemento es un usuario.
#Se crea una lista con la función split(), que nos pemite separar los elementos del string 'usuarios' por medio de comas.

listaUsuarios = usuarios.split(',')
print(listaUsuarios)

# •	Imprima en pantalla la cantidad usuarios que tiene tu aplicación.
#La función len() permite contar la cantidad de usuarios en la variable 'listaUsuarios'

print(len(listaUsuarios))

# •	Imprima en pantalla un mensaje de saludo a los diferentes usuarios. 
# ¿Qué técnica puedes utilizar para realizar esto?
# Una forma sería crear un mensaje para cada usuario, el cuál se localizaría en la lista. 

mensaje1 = 'Bienvenido a nuestro sitio ', listaUsuarios[0]
mensaje2 = 'Bienvenido a nuestro sitio ', listaUsuarios[1]
mensaje3 = 'Bienvenido a nuestro sitio ', listaUsuarios[2]
mensaje4 = 'Bienvenido a nuestro sitio ', listaUsuarios[3]
mensaje5 = 'Bienvenido a nuestro sitio ', listaUsuarios[4]
mensaje6 = 'Bienvenido a nuestro sitio ', listaUsuarios[5]
mensaje7 = 'Bienvenido a nuestro sitio ', listaUsuarios[6]

print(mensaje1)
print(mensaje2)
print(mensaje3)
print(mensaje4)
print(mensaje5)
print(mensaje6)
print(mensaje7)

#Otra forma sería aplicando un ciclo for; se crea la variable usuarios como contador, y luego se imprime el mensaje 
#con la variable 'usuario'

for usuario in listaUsuarios:
    print('---------------------')
    print('Bienvenido a nuestro sitio', usuario)

#También puede preguntarse directamente el nombre de usuario e imprimir este mensaje con su nombre

nomUsuario = input('Ingrese su nombre de usuario: ')
mensaje = 'Bienvenido a nuestro sitio', nomUsuario
print(mensaje)
