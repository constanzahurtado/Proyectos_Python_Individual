# DESARROLLO
# Como buen desarrollador, para comenzar a poder trabajar de manera óptima, es necesario que debamos preparar las 
# herramientas necesarias para inicializar nuestro proyecto, esto incluye tener ya nuestro editor de texto y la versión de
#  Python disponible en nuestro equipo.
# En esa ocasión se solicita un programa que:

# Pregunta el nombre de usuario y una contraseña.
# - Almacene ambos datos en una variable.
# - Que obtenga la edad del usuario a través de la consola. Sólo acepta números enteros.
# - Almacene el dato edad a cada usuario.
# - Imprima por cada usuario: su edad, y contraseña con un desfase de 5 segundos.
# El programa debe reiniciarse cada vez que termina. Sin perder la información anterior, debe continuar
# preguntando por nombre y contraseña.


import time

#Se inicializan las variables involucradas

nombre_usuario = '' # Se inicia la variable string
password_usuario = '' # Se inicia la variable string
usuarios = {} # Se crea un diccionario vacío

# Creación de una función que permita el registro de usuarios. 

def registro(): 
    global nombre_usuario #Se declaran variables globales y son utilizadas. 
    global password_usuario
    global usuarios
    nombre_usuario = input("Ingrese un nombre de usuario: ") # Se solicita un nuevo nombre de usuario.
    password_usuario = input("Ingrese una contraseña: ") # Se solicita contraseña de usuario.
    usuarios[nombre_usuario] = password_usuario # Los datos ingresados son agregados al diccionario.
    return usuarios # Se retorna el valor del diccionario. 

# Creación de una función que permita el ingreso de usuarios. 

def ingreso():
    global usuarios
    nombre_usuario_ingreso = input("Nombre de Usuario: ") # El usuario ya ingresado puede acceder a su cuenta ingresando su nombre de usuario
    password_usuario_ingreso = input("Contraseña: ") # y contraseña.
    
    for i,j in usuarios.items(): #Se inicia un ciclo para condicionar el ingreso del usuario.
        if i == nombre_usuario_ingreso and j == password_usuario_ingreso: # Si el usuario existe se le pedirá la edad.
            print("Bienvenido")
            edad = int(input("Por favor ingresa tu edad: "))
            usuarios[nombre_usuario_ingreso]=[password_usuario_ingreso, edad] # La edad se agrega al diccionario
            print(usuarios) # Se muestran los datos del usuario. 
        elif i == nombre_usuario_ingreso and j != password_usuario_ingreso: # Si el password es incorrecto, se indica que el campo es inválido.
            print("Campo inválido")
        elif i != nombre_usuario_ingreso and j == password_usuario_ingreso: # Si el usuario es incorrecto, se indica que el campo es inválido.
            print("Campo inválido")
        elif i != nombre_usuario_ingreso and j != password_usuario_ingreso: # Si ambos datos son incorrectos o no existe el usuario, se indica campor inválidos. 
            print("Campos inválidos")
        else:
            print("Error") # Captura errores de otra naturaleza. 

# Creación de una función que permita mostrar a los usuarios registrados. 

def imprimir_datos():
    for clave, valor in usuarios.items():   # Creación ciclo for para recorrer el diccionario de usuarios. 
        time.sleep(5)                # Permite mostar los usuarios con un desfase de 5 segundos.
        print(clave, valor)

while True: #Este ciclo while permite que el menú de opciones creado se repita hasta salir del programa
    print("Eliga una opcion. Para ello debe ingresar el número de la opción") # Menú de opciones
    print("1. Registrarme")
    print("2. Ingresar")
    print("3. Ver usuarios")
    print("4. Salir")
    opcion = input() #Ingreso de la opción.
    
    if opcion == "1": 
        registro() # Se llama a la función de registro.
        print("Usuario registrado")    
    elif opcion == "2":
        ingreso() # Se llama a la función de ingreso.
        print("Estos son tus datos")
    elif opcion == "3":
        print("Usuarios Registrados")
        imprimir_datos() # Se llama a la función imprimir_datos().
    elif opcion == "4":
        print("Hasta la Próxima")
        break #Esta opción interrumpe el ciclo
    else:
        print("Debe ingresar una opción para acceder. Recuerde que debe ser un número") # Si el usuario no ingresa un número, esta condición le indica el error.







  









 




