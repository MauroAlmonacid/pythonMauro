#1
print("-"*6,"LOGIN","-"*6)
user1="pedro"
pwrd1="1234"
user2="angel"
pwrd2="a4s1"

user=input("Usuario: ")
pwrd=input("Contraseña: ")

if user1==user and pwrd1==pwrd1 or user2==user and pwrd2==pwrd:
    print("Bienvenido!")
else:
    print("Usuario invalido.")

#2
print("-"*3,"CALCULADORA DE PROMEDIO","-"*3)

nota1=float(input("Ingrese la primera nota: "))
nota2=float(input("Ingrese la segunda nota: "))
nota3=float(input("Ingrese la tercera nota: "))

promedio=(nota1+nota2+nota3)/3

if promedio>=4.0:
    print(f"Su promedio es: {promedio.__round__(1)}")
    print("Ha Aprobado!")
else:
    print(f"Su promedio es: {promedio.__round__(1)}")
    print("Ha reprobado.")

#3
print("-"*6,"ALTERNATIVAS","-"*6)
print("""Cual de los siguientes animales viven en el agua?
      A)Perro
      B)Cocodrilo
      C)Conejo
      D)Tiburon""")

puntaje=0
resp=input("")

if resp=="d":
    puntaje=puntaje+1
    print("Correcto!")
elif resp=="b":
    puntaje=puntaje+0.5
    print("Correcto!")
else:
    print("Incorrecto.")

print(f"Tu puntaje fue: {puntaje}")

#4
print("-"*3,"PREGUNTAS DE EXTREMA DIFICULTAD","-"*3)
punt=0
print("""De que color es una manzana roja?
      A)Roja
      B)Fucsia
      C)Morado
      D)Verde""")
respuesta1=input("")
if respuesta1=="a":
    punt=punt+1
    print("Correcto!")
else:
    print("Incorrecto.")

print("""Cuantos dedos tiene una mano?
      A)3
      B)7
      C)14.709
      D)5""")
respuesta2=input("")
if respuesta2=="d":
    punt=punt+1
    print("Correcto!")
else:
    print("Incorrecto.")

print("""Cual es la 3ra letra del abecedario?
      A)C
      B)A
      C)5
      D)D""")
respuesta3=input("")
if respuesta3=="a":
    punt=punt+1
    print("Correcto!")
else:
    print("Incorrecto.")

print(f"Su puntaje ha sido: {punt}")

