import numpy as np
import os

def cargar_datos():
    mascotitas = np.empty((0, 7), dtype=object)
    try:
        with open('mascotitas.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                mascotitas = np.vstack([mascotitas, np.array(data)])
    except FileNotFoundError:
        print("Informacion.")
    return mascotitas

def guardar_datos(mascotitas):
    with open('mascotitas.txt', 'w') as file:
        for mascotitas in mascotitas:
            file.write(','.join(mascotitas) + '\n')


def ingresar_datos():
    nombre = input("Nombre de la mascota: ")
    codigo = input("codigo de la mascota: ")
    edad = input("Edad de la mascota: ")
    peso = input("peso de la mascota: ")
    raza = input("raza de la mascota: ")
    diagnostico = input("diagnostico de la mascota: ")
    medicamentos = input("Medicamentos recetados: ")

    nueva_ficha = np.array([[nombre, codigo, edad, peso, raza, diagnostico, medicamentos]])
    return nueva_ficha

def buscar_codigo(mascotitas, rut):
    mascotitas_encontrado = None
    for mascotitas in mascotitas:
        if mascotitas[1] == codigo:
            mascotitas_encontrado = mascotitas
            break
    return mascotitas_encontrado

def eliminar_ficha(mascotitas, codigo):
    mascotitas_actualizados = [mascotitas for mascotitas in mascotitas if mascotitas[1] != codigo]
    return np.array(mascotitas_actualizados)

def listar_mascotitas(mascotitas):
    for i, mascotitas in enumerate(mascotitas, start=1):
        print(f"Mascota {i}:")
        print(f"Nombre: {mascotitas[0]}")
        print(f"Codigo: {mascotitas[1]}")
        print(f"Edad: {mascotitas[2]}")
        print(f"peso: {mascotitas[3]}")
        print(f"raza: {mascotitas[4]}")
        print(f"diagnostico de la mascota: {mascotitas[5]}")
        print(f"Medicamentos recetados: {mascotitas[6]}")
        print()

listado_mascotitas = cargar_datos()

while True:
    print("Atencion medica veterinaria:")
    print("1. Crear ficha de la mascota")
    print("2. Buscar ficha por codigo de la mascota")
    print("3. Eliminar ficha de la mascota")
    print("4. Listar Mascotas atendidas")
    print("5. Salir")
    
    opcion = input("Ingrese el número de la opción deseada (1-5): ")

    if opcion == '1':
        listar_mascotitas=ingresar_datos
        print("Has ingresado la ficha correctamente")

    elif opcion == '2':
        codigo = input("Ingrese el codigo de la mascota para buscar: ")
        mascotitas_encontrado = buscar_codigo(listado_mascotitas,codigo)
        if mascotitas_encontrado is not None:
            print("Mascota encontrada:")
            print(f"Nombre: {mascotitas_encontrado[0]}")
            print(f"codigo: {mascotitas_encontrado[1]}")
            print(f"edad: {mascotitas_encontrado[2]}")
            print(f"peso: {mascotitas_encontrado[3]}")
            print(f"raza: {mascotitas_encontrado[4]}")
            print(f"diagnostico de la mascota: {mascotitas_encontrado[5]}")
            print(f"Medicamentos recetados: {mascotitas_encontrado[6]}")
        else:
            print("No se encontró ningúna mascota con ese codigo.")

    elif opcion == '3':
        rut = input("Ingrese el codigo para eliminar la ficha: ")
        listado_mascotitas = eliminar_ficha(listado_mascotitas, codigo)
        print("Ficha eliminada.")

    elif opcion == '4':
        if len(listado_mascotitas) > 0:
            print("Listado de mascotas atendidas:")
            listar_mascotitas(listado_mascotitas)
        else:
            print("No se encuentran mascotas registradas.")

    elif opcion == '5':
        guardar_datos(listado_mascotitas)
        print("Atencion finalizada...")
        break

    else:
        print("la opcion que as marcado no es valida Por favor, ingrese una opción del 1 al 5.")