while True:
    nom = input("Nombre: ")
    if nom == "":
        print("Error. Ingrese nombre.")
    elif len(nom) > 30:
        print("Error. Nombre debe tener 30 caracteres como máximo.")
    elif nom.isdigit():
        print("Error. El nombre no puede contener solo números.")
    else:
        break
#Se le pregunta el nombre al usuario, verificando que ingrese datos validos.

PagoHorExt = 0

while True:
    try:
        while True:
            sueldo = int(input("Sueldo Base: "))
            if sueldo < 0:
                print("Ingrese datos válidos.\n")
            else:
                break

        while True:    
            horas = int(input("Horas de trabajo mensuales: "))
            if horas < 0:
                print("Ingrese datos válidos.\n")
            else:
                break
            
        if horas > 180:
            horasExt = horas - 180
            pagoDia = sueldo / horas
            pagoExt = pagoDia * 0.5
            PagoHorExt = horasExt * pagoExt       
    except ValueError:
        print("Ingrese datos válidos.\n")
    else:
        break
#Se le pregunta el sueldo y las horas de trabajo al usuario, verificando que ingrese datos validos con el uso de try/except ValueError.

def calculo(sueldo, PagoHorExt):
    totalIngresos = sueldo + PagoHorExt
    descuentoFonasa = totalIngresos * 0.07
    descuentoAFP = totalIngresos * 0.10
    descuentoSeguridadSocial = descuentoFonasa + descuentoAFP
    sueldoNeto = totalIngresos - descuentoSeguridadSocial
    return totalIngresos, descuentoFonasa, descuentoAFP, descuentoSeguridadSocial, sueldoNeto
#Se realiza el calculo de la liquidacion de sueldo.

def desgloce(nom, sueldo, PagoHorExt, totalIngresos, descuentoFonasa, descuentoAFP, descuentoSeguridadSocial, sueldoNeto):
    print("\n------------------LIQUIDACIÓN----------------\n")

    print(f"Nombre:\t\t\t\t{nom}")
    print(f"Sueldo Base:\t\t\t${sueldo}")
    print(f"Pago Horas Extras:\t\t${int(PagoHorExt)}")
    print(f"Total de ingresos:\t\t${int(totalIngresos)}")
    print(f"Descuento por FONASA:\t\t${int(descuentoFonasa)}")
    print(f"Descuento por AFP:\t\t${int(descuentoAFP)}")
    print(f"Descuento por Seguridad Social:\t${int(descuentoSeguridadSocial)}")
    print(f"Sueldo Neto a pagar:\t\t${int(sueldoNeto)}")
#Se le muestra el la liquidacion al usuario.

totalIngresos, descuentoFonasa, descuentoAFP, descuentoSeguridadSocial, sueldoNeto = calculo(sueldo, PagoHorExt)
desgloce(nom, sueldo, PagoHorExt, totalIngresos, descuentoFonasa, descuentoAFP, descuentoSeguridadSocial, sueldoNeto)
#Se ejecutan las funciones del calculo y el desgloce.

with open(f"liquidacion_{nom}.txt", "w") as archivo:
    archivo.write("-----------LIQUIDACIÓN DE SUELDO---------\n")
    archivo.write(f"Nombre: {nom}\n")
    archivo.write(f"Sueldo Base: ${sueldo}\n")
    archivo.write(f"Pago Horas Extras: ${int(PagoHorExt)}\n")
    archivo.write(f"Total de ingresos: ${int(totalIngresos)}\n")
    archivo.write(f"Descuento por FONASA: ${int(descuentoFonasa)}\n")
    archivo.write(f"Descuento por AFP: ${int(descuentoAFP)}\n")
    archivo.write(f"Descuento por Seguridad Social: ${int(descuentoSeguridadSocial)}\n")
    archivo.write(f"Sueldo Neto a pagar: ${int(sueldoNeto)}\n")
#Se genera el archivo de texto con la liquidacion del sueldo
    
print(f"\nSe ha creado archivo de liquidación: liquidacion_{nom}.txt")
#Se le avisa al usuario sobre la creacion del archivo y su nombre.