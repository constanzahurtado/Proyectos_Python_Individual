
### Desarrollo Actividad Individual 3 ###

#Se define una variable lista para almacenar los tipos de formulario que puede responder un usuario

listaFormulario = []

#Se define los inputs de origen (si es de lationoamérica o no, edad y deportes que almacena la respuesta de afinidad por los deportes)

origen = input('¿Es usted originario de Latinoamérica? (S/N): ')
edad = int(input('Por favor ingrese su edad: '))
deportes = input('¿Le gustan los deportes? (S/N): ')


#Se elabora el flujo de condiciones
#Se toma como referencia el origen, luego la afinidad por los depotes y por último la edad. 

if origen == 's': #Si la persona procede de latinoamérica. 
    listaFormulario.append('Habitos Alimenticios') 
    if deportes == 's': #Si la persona tiene afinidad por el deporte. 
        if edad <= 60: #Condición por edad. 
            listaFormulario.append('Actividades Recreativas') # Se utiliza la función append para ingresar el formulario a la lista.
            listaFormulario.append('Natación')
        else:
            listaFormulario.append('Atletismo')          
    else: #Si la persona no tiene afinidad por el deporte.
            listaFormulario.append('Deportes en General')
    if edad >=18 and edad <=29:
        listaFormulario.append('Empleabilidad')
    elif edad >=30 and edad <=59:
        listaFormulario.append('Experiencia Laboral') 
else: #Si la persona no procede de latinoamérica. 
    if deportes == 's': #Si la persona tiene afinidad por el deporte. 
        if edad <=60:
            print('Atletismo')
        if edad >=18 and edad <=29:
            print('Deportes en General')
    else: #Si la persona no tiene afinidad por el deporte. 
        print('Deportes en General')
        if edad >=18 and edad <=29:
            print('Empleabilidad')

#Una vez que se ejecuta el primer flujo, se imprimen las variables almacenadas en la lista de formularios.

if len(listaFormulario) > 3: #Se condiciona para que la lista impresa sólo arroje 3 formularios. 
    print(listaFormulario[0:3])  
else:
    print (listaFormulario) #Si no tiene más de 3 formularios, se imprime toda la lista.

