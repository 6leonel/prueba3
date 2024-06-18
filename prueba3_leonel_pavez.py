#Evaluación Parcial N°3 Forma-A
#Leonel Pavez
#FPY1101  Fundamentos de Programación

import csv
from datetime import datetime

reclamos = []

def menu():
    print("Bienvenido al Sistema de Reclamos del SERNAC")
    print("1. Registrar Reclamo")
    print("2. Listar Reclamos")
    print("3. Respaldar Reclamos")
    print("4. Salir")

def registrar_reclamo():
    rut = input("Ingrese RUT del reclamante con DV: ")
    monto = float(input("Ingrese el monto de la compra en miles de pesos: "))
    reclamo = input("Ingrese la reseña del reclamo (máximo 20 caracteres): ")

    fecha = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    reclamos.append({'RUT': rut, 'Fecha': fecha, 'Monto': monto, 'Reclamo': reclamo})

    print("Reclamo registrado correctamente.")

def listar_reclamos():
    if not reclamos:
        print("No hay reclamos registrados.")
    else:
        print("Listado de Reclamos:")
        for reclamo in reclamos:
            print(f"RUT: {reclamo['RUT']} | Fecha: {reclamo['Fecha']} | Monto: {reclamo['Monto']} | Reclamo: {reclamo['Reclamo']}")

def respaldar_reclamos():
    if not reclamos:
        print("No hay reclamos para respaldar.")
        return
    
    nombre_archivo = input("Ingrese el nombre para el archivo de respaldo (sin extensión): ")
    nombre_archivo += ".csv"

    try:
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(['RUT', 'Fecha', 'Monto', 'Reclamo'])
            for reclamo in reclamos:
                writer.writerow([reclamo['RUT'], reclamo['Fecha'], reclamo['Monto'], reclamo['Reclamo']])
        print(f"Reclamos respaldados en el archivo {nombre_archivo} correctamente.")
    except IOError:
        print(f"No se pudo escribir en el archivo {nombre_archivo}. Verifique los permisos.")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        registrar_reclamo()
    elif opcion == '2':
        listar_reclamos()
    elif opcion == '3':
        respaldar_reclamos()
    elif opcion == '4':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")

print("Programa finalizado.")
