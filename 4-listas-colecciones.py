#Jade Pacompia
#Listas
lista = ["Jade","Pacompia",25,True]
print(lista[0])
#Lista de frutas
frutas = ["Manzana", "Pera", "Platano", "Mango", "Papaya"]
print(frutas[3])

frutas[1] = "Granada"
print(frutas)
#Matriz
matriz = [
    [1,2,3],
    [4,6,1],
    [0,1,0]
]
print(matriz[2][2])

#Lista de numeros
numeros = [1,2,3,4,5,6,7,8,9,0]
print(numeros[8])
print(numeros[:3])
print(numeros[1:5])
print(numeros[::2])
print(numeros[::-1])

#Ciclo for en las listas
for i in numeros:
    print(i*10)

for i in frutas:
    print(i)

#metodos en las listas 
print("------------------------------------Metodos")
frutas = ["Manzana", "Pera", "Platano", "Mango", "Papaya"]

#agregar un nuevo dato
frutas.append("Ciruela")
print(frutas)

#insert
frutas.insert(2,"Palta")
print(frutas)

#remove = borrar un dato
frutas.remove("Mango")
print(frutas)

#pop = para obtener o eliminar un dato
frutas.pop()
print(frutas)

#sort() = ordenar las listas
frutas.sort()
print(frutas)

#reverse() = revertir
frutas.reverse()
print(frutas)

#Len() = contar datos
cantidad = len(frutas)
print(cantidad)

#index() = 
indice = frutas.index("platano")
print(indice)