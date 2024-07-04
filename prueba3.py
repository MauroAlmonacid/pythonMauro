class Reserva:
    def __init__(self, nombre, ciudad_origen, tour, cantidad_personas):
        #Agrega argumentos de nombre, ciudad de origen, cantidad de presonas
        self.nombre = nombre
        self.ciudad_origen = ciudad_origen
        self.tour = tour
        self.cantidad_personas = cantidad_personas
#Crea instancia de reserva con los detalles

def reg_reserva():
    #Funcion para que el cliente registe una reserva
    nombre=input("Nombre y apellido del cliente: ")
    ciudad_origen=input("Ciudad de origen: ")
    tour=input("Detalle del tour (Torres del Paine, Carretera Austral o Chiloé): ")
    cantidad_personas=int(input("Cantidad de personas: "))

    #Validación de datos
    if not nombre or not ciudad_origen or not tour:
        print("Error: Todos los datos deben ser ingresados.")
        return None
    return Reserva(nombre, ciudad_origen, tour, cantidad_personas)

def listar_reservas(reservas):
    #Funcion para mostrar las reservas registradas y sus detalles
    print("\nReservas registradas:")
    for reserva in reservas:
        print(f"{reserva.nombre}-{reserva.ciudad_origen}/{reserva.tour} ({reserva.cantidad_personas} personas)")
        #Muestra nombre del cliente, ciudad de origen, destino y cantidad de  personas
def generar_archivo(destino, reservas):
    #Funcion para crear un archivo de texto con los detalles de las reservas
    nombre_archivo = f"{destino.lower().replace(' ', '_')}_reservas.txt"
    with open(nombre_archivo,"w") as archivo:
        archivo.write("Reservas " + destino + "\n")
        for reserva in reservas:
            if reserva.tour.lower()==destino.lower():
                archivo.write(f"{reserva.nombre} - {reserva.ciudad_origen}/{reserva.destino} ({reserva.cantidad_personas} personas)\n")
        #Escribe el archivo de texto
    print(f"Archivo {nombre_archivo} ha sido creado exitosamente.")

def main():
    reservas=[] 
    destinos=["Carretera Austral", "Chiloé", "Torres del Paine"] #Destinos disponibles

    while True:
        print("")
        print("-----------------------------MENU-----------------------------")
        print("1. Registrar Reserva")
        print("2. Listar Todas las Reservas")
        print("3. Detalles de Reservas por Destino")
        print("4. Salir del Programa")
        #Se muestra el menu y las opciones
        opcion=input("Seleccione una opción (1-4): ")
        #Registra la opcion seleccionada

        if opcion=="1":
            reserva=reg_reserva() #Opcion 1
            if reserva:
                reservas.append(reserva)
                print("Reserva registrada.")
        elif opcion=="2":
            listar_reservas(reservas) #Opcion 2
        elif opcion=="3":
            destino=input("Escriba el destino: \n Torres del Paine \n Carretera Austral \n Chiloé\n") #Opcion3
            if destino in destinos:
                generar_archivo(destino, reservas)
            else:
                print("Destino inválido. Intente nuevamente.")
        elif opcion=="4":
            print("Cerrando...") #Opcion 4
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__=="__main__":
    main()
