print("-"*10,"VENTA DE TICKETS","-"*10,"\nBienvenido!")

while True:
    try:
        cantTick=int(input("Cantidad de tickets que desea vender: "))
        break
    except ValueError:
        print("Error, ingrese un numero.") 
        
totalPrecio = 0

for x in range(1,cantTick+1):
    while True:
        try:
            precioTick=float(input(f"Ingrese el precio del ticket numero {x}: "))
            totalPrecio+=precioTick
            break
        except ValueError:
            print("Por favor, ingrese un numero.")
print("-"*40)
print(f"INGRESOS TOTALES: ${int(totalPrecio)}")
