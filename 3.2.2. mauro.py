print("-------------ACT1------------")
nombres=[]
for i in range(3):
    nombre=input("Ingresa un nombre: ")
    nombres.append(nombre)  

nombre_mas_largo=max(nombres, key=len)

print(f"El nombre con la mayor cantidad de caracteres es: {nombre_mas_largo}")

print("-------------ACT2------------")
names = []
apellidos = []

for i in range(3):
    names.append(input("Ingrese nombre: "))
    apellidos.append(input("Ingrese apellido: "))

names.sort()
apellidos.sort()

print("\nNombres:")
for name in names:
    print(name)

print("\nApellidos:")
for apellido in apellidos:
    print(apellido)

print("-------------ACT3------------")

while True:
    nombre = input("Ingresa un nombre: ")
    nombres.append(nombre)
    
    
    respuesta = input("¿Deseas agregar otro nombre? (sí/no): ").lower()
    if respuesta != 'sí':
        break

if nombres:
    nombre_menor = min(nombres, key=len)
    nombres.remove(nombre_menor)

print("Lista de nombres después de eliminar el más corto:")
for nombre in nombres:
    print(nombre)
