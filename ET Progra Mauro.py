#se importa la funcion random para luego usarla al generar sueldo
import random

#se importa math para poder usar funciones matematicsas  dentro del code
import math

#se importa csv para poder crear un archivo de texto con los datos
import csv

#lista de trabajadores
trabajadores = [
    {"nombre":"Juan Perez"},
    {"nombre":"Maria Garcia"},
    {"nombre":"Carlos Lopez"},
    {"nombre":"Ana Martinez"},
    {"nombre":"Pedro Rodrigez"},
    {"nombre":"Laura Hernandez"},
    {"nombre":"Miguel Sanchez"},
    {"nombre":"Isable Gomez"},
    {"nombre":"Francisco Diaz"},
    {"nombre":"Elena Ferndandez"}
]

#funcion para genrar sueldo aleatorio, opcion 1 menu
sueldos=[]
def sueldo_random():
    global sueldos
    sueldos=[random.randint(300000,2500000)for _ in range(10)]
    return sueldos

#funcion para clasificar sueldos, opcion 2 menu
def clasif_sueldo():
    #se muestran lo sueldos menores a 800000
    print("\nSueldos menores a $800000 TOTAL:",len([s for s in sueldos if s<800000]))
    print("Nombre:\t\t Sueldo:")
    for trabajador,sueldo in zip (trabajadores,sueldos):
        if sueldo<800000:
            print(f"{trabajador['nombre']}\t ${sueldo}")
    
    #se muestran los sueldos entre 800000 y 2000000
    print("\nSueldos entre $800000 y $2000000 TOTAL:", len([s for s in sueldos if s>=800000 and s<=2000000]))
    print("Nombre:\t\t Sueldo:")
    for trabajador,sueldo in zip (trabajadores,sueldos):
        if sueldo>=800000 and sueldo<=2000000:
            print(f"{trabajador['nombre']}\t ${sueldo}")

    #se muestran los sueldos superiores a 2000000
    print("\nSueldos superiores a $2000000 TOTAL",len([s for s in sueldos if s>2000000]))
    print("Nombre:\t\t Sueldo:")
    for trabajador,sueldo in zip(trabajadores,sueldos):
        if sueldo>2000000:
            print(f"{trabajador['nombre']}\t ${sueldo}")
    sueldo_total=sum(sueldos)
    print(f"\nTotal Sueldos: ${sueldo_total}")

    

#funcion para ver estadisticas, opcion 3 menu
def stats():
    max_sueldo=max(sueldos) #variable para determinar cual es el sueldo mayor
    min_sueldo=min(sueldos)#variable para determinar cual es el sueldo menor
    mid_sueldo=sum(sueldos)/len(sueldos) #variable para calcular el promedio de los sueldos
    med_geo=math.exp(sum(math.log(sueldo) for sueldo in sueldos)/len(sueldos)) #variable para calcular la media geometrica
    print(f"Sueldo mas alto:\t{max_sueldo}\nSueldo mas Bajo:\t{min_sueldo}\nPromedio de sueldos:\t{mid_sueldo}\nMedia geometrica:\t{med_geo}")

#funcion para generar archivo csv con el reporte de sueldos.
def report():
    with open('reporte_sueldos.csv','w',newline="")as file:
        writer=csv.writer(file)
        writer.writerow(["Nombre empleado","Sueldo base","Descuento salud","Descuento AFP","Sueldo liquido"])
        for trabajador,sueldo in zip(trabajadores,sueldos):
            #se procesa la liquidacion del sueldo
            salud=sueldo*0.07
            afp=sueldo*0.12
            liquid=sueldo-salud-afp
        writer.writerow([trabajador["nombre"], int(sueldo), int(salud), int(afp), int(liquid)])
        print('Archivo "reporte_sueldos.csv" creado exitosamente.') #notifica al usuario que el archivo ha sido creado

sueldo_random() #invoco la funcion para generar sueldos random para que el usuario pueda usar otras opciones sin tener que seleccionar opcion 1 primero

#menu de opciones    
print("-"*25,"MENU","-"*25)
print("1. Asignar sueldos aleatorios.\n2. Clasificar sueldos.\n3. Ver estadisticas.\n4. Reporte de sueldos.\n5. Salir")


while True: #este while lo usare para que el usuario pueda ingresar tantas opciones como quiera, hasta que decida salir del programa
    error=0 #usare esta variable para determinar si ha habido error en lo ingresado por el usuario
    while error==0:
        #se usa un try/except con ValueError para que el programa no pare al ingresar un valor invalido
        try:    
            resp_menu=int(input(">"))
            error=1
        except ValueError: 
            print("Ingrese opcion valida.")
        
    if resp_menu==1: #opcion 1 del menu
        sueldo_random()
    elif resp_menu==2: #opcion 2 del menu
        clasif_sueldo()
    elif resp_menu==3: #opcion 3 del menu
        stats()
    elif resp_menu==4:
        report()
    else:
        print("\nCerrando programa...\nDesarrollado por Mauro Almonacid\n21.687.996-1") #salir del menu
        break