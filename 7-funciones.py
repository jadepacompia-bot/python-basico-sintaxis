#Jade Pacompia
#FUnciones
print('hola, Juan')
print('Bienvenido al sistema')
print('--------')
pass
print('hola, nombre')
print('Bienvenido al sistema')
print('--------')
pass
print('hola, Pepito')
print('Bienvenido al sistema')
print('--------')
pass
def saludar():
    print("Hola, ", )
    print("Bienvenido al sistema")
    print('--------')

#Correct
lista_nombres = ["Juan", "Emily", "Pepito"]
for i in lista_nombres:
        print('-------------')
        print('Hola,', i)
        print('Bienvenido al sistema')
        print('-------------')
print('.........')
def saludar(variable):
      print('Hola,', variable)
      print('Bienvenido al sistema')
      print('---------------')
saludar("Juan")
saludar("Emily")
saludar("Pepito")

#funciones con retorno-return()
def suma(primer_numero,segundo_numero):
      resultado = primer_numero + segundo_numero
      return(resultado)
print(suma(2,3))
#Funciones sin retorno
def suma2(fisrt_number, second_number):
      result = fisrt_number + second_number
      print(result)
suma2(2,2)