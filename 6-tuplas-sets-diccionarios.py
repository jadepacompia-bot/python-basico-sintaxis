#Jade Pacompia
#Tuplas y diccionarios
#-Tuplas-
#SImbolos ()
#por default la ordena
#inmmutables = no se puede hacer cambios
#te acepta duplicados
tupla = (1,2,1,2,40,10,5,11)
print(tupla)
#indices
print(tupla[4])
# -Sets-
# simbolo {}
#no ordena
#mutable = puedes modificarlo
#no acepta duplicados
sets = {1,2,3,1,2,3}
print(sets)
sets.add(4) #agregar un nuevo dato
print(sets)
sets.remove(2) #remueve un dato
print(sets)
#-Diccionarios-
#simbolo {key:value}
#ordena por default
estudiante = {
    'nombre': 'jade',
    'birthplace': 'Puno',
    'edad': 20,
    'carrera': 'ingenieria de software'
}
print(estudiante)
print(estudiante['nombre'])
print(estudiante['birthplace'])
print(estudiante['edad'])
print(estudiante['carrera'])
estudiante['edad'] = 50
print(estudiante)
#ciclo for en los diccionarios
for clave, valor in estudiante.items():
    print('Clave:', clave, 'Valor:', valor)