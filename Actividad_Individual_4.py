
# DESARROLLO OPCIÓN 1:
# Nuestra aplicación tendrá la siguiente particularidad. Al momento de crear un usuario, este debe ingresar una 
# contraseña que esté acorde a nuestros criterios de seguridad.
# En este sentido, la contraseña debe contar con al menos 8 caracteres, con mayúsculas, minúsculas y cifras.
# Nuestro programa debe indicarle al usuario qué criterios le faltan para disponer de una contraseña segura.
# La contraseña debe ingresarse carácter por carácter en el terminal. Luego de escribir cada carácter, el programa 
# envía un mensaje con los criterios aún incumplidos.

#Se crean listas con los caracteres necesarios para una contraseña segura

numeros =['0','1','2','3','4','5','6','7','8','9']
mayusculas= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Se inicia un ciclo while con una condición booleana True

while True:
  password = input("Ingrese una contraseña. Recuerde que debe tener al menos una mayúscula y un número: ")#Variable contraseña
  passwordValido = False #Mientras el password válido se falso se considerarán las siguientes condiciones: 

  if (len(password)<8 or len(password)>12): #Longitud de password entre 8 y 12 caracteres
      print("Su password debe tener entre 8 y 12 caracteres")    
#Para validar los caracteres, utilizamos la función any(), que permite devolver False si un objeto iterable no existe.
# más un not, que permite junto con el ciclo for, verificar si el caracter se encuentra en la lista correspondiente.  
#Se realiza un ciclo
  elif not any(numero in numeros for numero in password):
        print('Su contraseña debe tener al menos un número')
  elif not any(mayus in mayusculas for mayus in password):
        print('Su contraseña debe tener al menos una mayúscula')
  elif not any(minus in minusculas for minus in password):
        print('Su contraseña debe tener al menos una minúscula')
  else: #Si la condición en while es verdadera, se valida la contraseña como correcta
      passwordValido = True
      print('Su contraseña es válida')
      break #Se termina el loop while con un break, y si la variable passwordValido es True





