import json
import csv

mayores=[]

with open('datos1.csv','r') as archivo:
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