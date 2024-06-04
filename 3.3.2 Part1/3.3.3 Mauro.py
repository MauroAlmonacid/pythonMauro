import csv
import json

def crearCsv(nombreCsv1,datos1):
    with open(nombreCsv1, 'w', newline='')as archivo:
        writeCsv=csv.writer(archivo)
        writeCsv.writerows(datos1)
    print("Archivo creado exitosamente.")

def leerCsv(nombreCsv):
    with open(nombreCsv, 'r') as archivo:
        return list(csv.reader(archivo))
    
datos=[
    ["Nombre","Edad","Comuna"],
    ["Juan",21,"Puente Alto"],
    ["Maria",30,"Concepcion"],
    ["Carlos",22,"Viña del Mar"],
    ["Estela",25,"Puerto Montt"]
]

crearCsv('datos1', datos)

mayores=[]

with open('datos1','r') as archivo:
    lector_csv=csv.DictReader(archivo)

    for fila in lector_csv:
        nombre=fila['Nombre']
        edad=int(fila['Edad'])
        Comuna=fila['Comuna']
        estado_edad="Mayor de Edad" if edad>=18 else "Menor de Edad"

        print(f"{nombre} tiene {edad} años ({estado_edad}) y es de {Comuna}")

        if edad>=25:
            mayores.append({
                'Nombre':nombre,
                'Edad':edad,
                'Comuna':Comuna
            })

with open('mayores','w') as archivoJson:
    json.dump(mayores, archivoJson, indent=1)