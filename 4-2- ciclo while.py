
while False:
    print('Jade')

#Valida Contraseña
password_correcta = "123456"
intentos = 0

while True:
    password = input("ingrese porfavor su constraseña: ")
    intentos += 1
    if (password == password_correcta):
        print("contraseña correcta 👍👍👍")
    else:
        print("contraseñsa incorrecta 😭😭😭")
        if(intentos >=3):
            print("tarjeta bloqueada 🤷‍♀️🤷‍♀️🤷‍♀️")
            break
        
 
 





