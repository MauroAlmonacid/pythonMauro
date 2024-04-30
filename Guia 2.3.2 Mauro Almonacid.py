#Ejercicio 1
print("-"*6,"Ejercicio 1","-"*6)
edad = int(input ("Ingrese su edad: "))
if edad > 0 and edad < 18:
    print(f"Edad: {edad} ,tiene descuento de un 50% ")
elif edad > 18 and edad < 30:
    print (f"Edad: {edad} ,tiene descuento de un 20%")
elif edad >= 60:
    print (f"Edad: {edad} ,tiene descuento de un 90%")
else:
    print (f"Edad: {edad} ,no aplica descuento")

#Ejercicio 2
print("-"*6,"Ejercicio 2","-"*6)
user = input("Ingrese su user: ")
pwd = input("Ingrese su pass: ")

if user=="mauro"and pwd=="1234":
    print ("Bienvenido")
else:
    print ("Error en contraseña")

#Ejercicio 3
print("-"*6,"Ejercicio 3","-"*6)

user = input("Ingrese el usuario: ")
pwd = input("Ingrese su password: ")
if user == "duoc" and pwd == "123duoc":
    valorDev = int(input("Bienvenido, Ingrese el valor a devolver: "))
    if valorDev > 100000:
        print("Se dará la máxima urgencia a su devolución de dinero")
    else:
        print("El caso ha quedado registrado, le informaremos lo antes posible")
else:
    print("Error en contraseña")

#El mensaje que daria seria: "Se dará la máxima urgencia a su devolución de dinero"