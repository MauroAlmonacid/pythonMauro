import csv
import json

def crear_csv(nombre_csv, datos):
    with open(nombre_csv, 'w', newline='') as archivo:
        write_csv = csv.writer(archivo)
        write_csv.writerows(datos)
    print("Listado creado exitosamente.")

def leer_csv(nombre_csv):
    with open(nombre_csv,'r') as archivo:
        return list(csv.reader(archivo))
    
datos = [
    ["run", "nombre"],   
    ["10744679-6", "Jose Haro"],
    ["19881120-3", "Daniela Almonacid"],
    ["16112356-0", "Carlos González"],
    ["17651562-7", "Andrea Soto"],
    ["13429495-7", "Luis Torres"],
    ["17470063-K", "Maria Rodríguez"],
    ["19089980-2", "Pablo Fernández"],
    ["17449807-5", "Valentina Pérez"],
    ["13154134-1", "Nicolás Vargas"],
    ["14073175-7", "Antonella Muñoz"],
    ["24052019-2", "Felipe Silva"],
    ["27779771-2", "Sofía López"],
    ["23135155-8", "Juan Díaz"],
    ["25449950-1", "Isabel Castro"],
    ["22398351-0", "Diego Morales"],
    ["20449542-4", "Ana Smith"],
    ["27730053-2", "Matías Araya"],
    ["27358198-7", "Valeria Mendoza"],
    ["25130662-1", "Gabriel Pérez"],
    ["24981167-K", "Martina Ruiz"],
    ["22096175-3", "Sebastián Herrera"],
    ["23010574-K", "Francisca Flores"],
    ["24218263-4", "Ricardo González"],
    ["28942147-5", "Constanza Álvarez"],
    ["27165749-8", "Javiera Troncoso"],
    ["22216307-2", "Eduardo Navarro"],
    ["22425010-K", "Catalina Vargas"],
    ["23811768-2", "Ángela Soto"],
    ["24661213-7", "Cristian Mora"],
    ["20781422-9", "Carla Contreras"],
    ["10363927-1", "Mauricio Rojas"],
    ["12598545-9", "Marcela Fernández"],
    ["19105327-3", "Felipe Montes"],
    ["19539754-6", "Alejandra Oyarzún"],
    ["15731749-0", "Pedro Ramírez"],
    ["12865638-3", "Daniela Aravena"],
    ["10294021-0", "Francisco Valdés"],
    ["14104975-5", "Florencia Rojas"],
    ["11975810-6", "Rodrigo Gómez"],
    ["17500269-3", "Amanda Guzmán"]
]

def encontrar_ganadores(datos):
    ganadores=[]
    for dato in datos[1:]:
        run=dato[0]
        digitos_verificadores=["92", "95", "84"]
        for digito_verificador in digitos_verificadores:
            if run[-4:-2]==digito_verificador:
                ganadores.append(dato)
                break
    return ganadores


def guardar_json(nombre_json, datos):
    ganadores_json=[]

    for dato in datos:
        ganador = {"run":dato[0],"nombre":dato[1]}
        ganadores_json.append(ganador)

    print("Datos de los ganadores:",ganadores_json)

    with open(nombre_json,'w') as archivo:
        json.dump(ganadores_json,archivo, indent=4)
    print("Ganadores guardados exitosamente en el archivo JSON.")

ganadores=encontrar_ganadores(datos)

guardar_json("ganadores.json", ganadores)

print(ganadores)