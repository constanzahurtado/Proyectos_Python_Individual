# Diseñe 7 diccionarios, donde el nombre de cada diccionario es el nombre de un usuario de su aplicación.
# En cada diccionario, integre características como: edad, género y otras características particulares de su aplicación.
# Por ejemplo, si la aplicación se enfoca en Juntas de Vecinos integrar dirección y número telefónico. Integre al menos
#  cinco características.
# Guarde estos diccionarios en una lista. En el caso de ejemplo, podría ser nombrada “JJVV”.
# A continuación, recorra su lista e imprima toda la información que posee la estructura de datos sobre cada usuario
#  (en el caso de ejemplo: de cada junta de vecinos).
# ¿Qué problemas encontró con esta forma de almacenar la información?

# Creación de una lista con diccionarios, utilizando como clave el nombre de los usuarios y valor una lista que almacena
# la edad, género, número telefónico, correo electrónico. 

usuarios = [{'Antonio':[32,'masculino','912345678','antonio@gmail.com']},
        
        {'María':[21,'femenino','932165498','maria@gmail.com']},
     
        {'Juan':[36,'masculino','941256387','juan@gmail.com']},
      
        {'Sara':[48,'femenino','985214778','sara@gmail.com']},
       
        {'Marcela':[30,'femenino','985214736','marcela@gmail.com']},
      
        {'Roberto':[50,'masculino','985236974','roberto@gmail.com']},
      
        {'Diego':[68,'masculino','912335785','diego@gmail.com']},

]

#Ciclo for para imprimir los elementos de la lista "usuarios"    

for i in usuarios:
    print(i)

# Almacenar la información de esta forma puede generar duplicado de datos, ya que la lista no tiene un identificador único.
# No es posible realizar un output de keys y values de cada diccionario de forma directa. 
# Del punto anterior, se podría dificultar la manipulación de datos cuando sea necesaria.  
#--------------------------------------------------------------------------------------------------------------------------------------------

# Vuelva al inicio del problema y diseñe una estructura de datos unificada que permita almacenar todas las juntas de 
# vecinos.
# Agregue para cada usuario los campos nombre_usuario, id_unico, antigüedad, fecha de incorporación.

print('------------------------------------------------------------------------------------------------------------------')

#Creación diccionario con usuarios, clave id_único y valor una lista que almacena
# nombre de ususario, la edad, género, número telefónico, correo electrónico, antigüedad, fecha de incorporación.  

usuarios2 = {'17.112.369-9':['Antonio',32,'masculino','912345678','antonio@gmail.com',3,'25-10-2018'],

        '20.235.369-5':['María',21,'femenino','932165498','maria@gmail.com',4,'10-09-2017'],

        '16.214.369-6':['Juan',36,'masculino','941256387','juan@gmail.com',2,'11-02-2019'],

        '14.258.369-5':['Sara', 48,'femenino','985214778','sara@gmail.com',3,'04-06-2018'],

        '17.258.369-9':['Marcela',30,'femenino','985214736','marcela@gmail.com',4,'03-07-2017'],

        '16.321.456-9':['Roberto',50,'masculino','985236974','roberto@gmail.com',1,'07-07-2020'],

        '5.023.369-9':['Diego',68,'masculino','912335785','diego@gmail.com',2,'05-07-2019',],
}

# Imprima en pantalla la fecha de incorporación de todos los usuarios.

#Ciclo for para imprimir las fechas del diccionario "usuarios2"    

for values in usuarios2.values():
    print(values[-1])