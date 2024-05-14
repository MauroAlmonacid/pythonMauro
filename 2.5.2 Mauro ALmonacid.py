#EJERCICIO 1
print("--------------------EJERCICIO 1--------------------\n")
puntos = 100000

print("1. Ver mis puntos")
print("2. Gastar mis puntos")
print("3. Salir")

while True:
    opcixn=int(input("=>"))
    
    if opcixn==1:
        print(f"PUNTOS: {puntos}")
    elif opcixn==2:
        print("\nSeleccione el producto a canjear")
        print("1.- Gift Card de $10.000, valor de 10.000 puntos")
        print("2.- Secadora de pelo, valor de: 25.000 puntos")
        print("3.- Disco duro portátil, valor de: 30.000 puntos\n")
        print("4.- Salir.")

        while puntos>10000:  
            continua = int(input("Seleccione un producto: "))
            if continua==1:
                puntos = puntos-10000
                print(f"Canje exitoso, le quedan: ${puntos} puntos\n")
            elif continua==2:
                puntos = puntos-25000
                print(f"Canje exitoso, le quedan: ${puntos} puntos\n")
            elif continua==3:
                puntos = puntos-30000
                print(f"Canje exitoso, le quedan: ${puntos} puntos\n")
            elif continua==4:
                break    
    elif opcixn==3:
        print("Saliendo...")
        break

#EJERCICIO 2
print("\n\n\n----------------------EJERCICIO 2-------------------\n")
saldo=500000
def banco(saldo):
    while True:

        print("-------------BANCO-------------")
        print("Seleccione una de las opciones:")
        print("1.-Ver saldo")
        print("2.-Retirar dinero")
        print("3.-Salir")
        while True:
            try:
                opcion=int(input("=>"))
                break
            except ValueError:
                print("Ingrese una opcion valida\n")
        
        if opcion==1:
            print(f"\nSu saldo: ${saldo}\n")
            
            print("Volver(1) Salir(2)")
            while True:
                try:    
                    volsal=int(input("=>"))
                    break
                except ValueError:
                    print("Ingrese una opcion valida.")
            if volsal==1:
                banco(saldo)
            elif volsal==2:
                print("\nCierre de sesion exitoso,adios.")
                break
            else:
                print("Ingrese opcion valida.")
        elif opcion==2:
            retiro=int(input("Ingrese la cantidad que desee retirar: "))
            if saldo>=retiro:
                saldo=saldo-retiro
                print("\nRetiro realizado.\n")
            else:
                print("\nNo hay saldo suficiente.\n")  
              
            print("Volver(1) Salir(2)")
            try:
                volsal=int(input("=>"))
            except ValueError:
                print("Ingrese una opcion valida.")
            if volsal==1:
                banco(saldo)
            elif volsal==2:
                print("\nCierre de sesion exitoso,adios.")
                break
            else:
                print("Ingrese opcion valida.")
        elif opcion==3:
            print("Cierre de sesion exitoso.")
            break        
        else:
            print("Ingrese una opcion valida.")

banco(saldo)

#EJERCICIO 3
print("\n\n\n----------------------EJERCICIO 3----------------------\n")
sw = 1
saldx = 0
while sw==1:
    print("1. Ver mi Saldo")
    print("2. Cargar Saldo")
    print("3. Salir")
    try:
        op=int(input("Seleccione una opción: "))
    
        if(op > 0 and op < 4):
            if op == 1:
                print(f"Tiene un saldo de {saldx}")
                continu = int(input("Presione 1) para volver atrás, Presione 2) para salir: "))
                if continu==2:
                    print("Cierre de sesión exitoso, adiós")
                    sw=0
        if op == 2:
            print("¿Cuánto desea cargar?")
            print("1.- $1.000")
            print("2.- $5.000")
            print("3.- $20.000")
            
            continu = int(input("Seleccione la opción: "))
            if continu==1:
                saldx = saldx+1000
                print(f"Carga exitosa, su saldo es de: ${saldx}")
            if continu==2:
                saldx = saldx+5000
                print(f"Carga exitosa, su saldo es de: ${saldx}")
            if continu==3:
                saldx=saldx+20000
                print(f"Carga exitosa, su saldo es de: ${saldx}")

        if op == 3:
            print("Muchas gracias por ocupar el servicio, adiós.")
            sw=0
        elif op>3:
            print("Selección fuera de rango")
    except ValueError:
        print("Ingreso Erróneo\n")