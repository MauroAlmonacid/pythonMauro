#-------------------------------------------------------------------------------------
#(16/04/2024)
"""
EJERCICIOS (16/04/2024)
1.-Convertir temperatura d farenheit a celcius.

2.-Calcular la edad exacta del usuario.
"""
#EJERCICIO 1

tempF = int(input("Dame tu temperatura en farenheit: "))
tempC = (tempF - 32) * 5/9
print("Tu temperatura en C° es:", tempC, "C°")

#EJERCICIO 2

añoNacimiento = int(input("Ingrese su año de nacimiento: "))
cumple = input("Usted ha tenido su cumpleaños este año? ")
if cumple == "si":
 añoNacimiento = 2024 - añoNacimiento

if cumple == "no":
 añoNacimiento = 2023 - añoNacimiento

print("Usted tiene", añoNacimiento, "años.")

#---------------------------------------------------------------------------------
#(18/04/2024)
"""
#EJERCICIOS 
1.-Calcular los dias de vida en base a mi edad.
2.-Crear una calculadora basica + - * / con funciones.
"""

#EJERCICIO 1

edad = int(input("Ingrese su edad: "))

diasVida = edad*365
print("Usted tiene ", diasVida, "dias de vida.")

#EJERCICIO 2
print("CALCULADORA")
num_1 = int(input())
num_2 = int(input())

def sumar():
    resultado = num_1+num_2
    print("=", resultado, "(SUMA)")

def restar():
    resultado = num_1-num_2
    print("=",resultado, "(RESTA)")

def multiplicar():
    resultado = num_1*num_2
    print("=", resultado, "(MULTIPLICACION)")

def dividir():
    resultado = num_1/num_2
    print("=", resultado, "(DIVISION)") 

sumar()
restar()
multiplicar()
dividir()