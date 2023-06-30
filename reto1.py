"""
def agregar_pasajeros(pasajeros):
    nombre = input("Ingrese el nombre del pasajero: ")
    identificacion = int(input("Ingrese la identificación del pasajero: "))
    destino = input("Ingrese el destino del pasajero: ")
    pasajero = (nombre, identificacion, destino)
    pasajeros.append(pasajero)
    return pasajeros

def agregar_ciudades(ciudad):
    nombre_ciudad = input("Ingrese el nombre de la ciudad: ")
    nombre_departamento = input("Ingrese el nombre del departamento: ")
    ciudad_nueva = (nombre_ciudad, nombre_departamento)
    ciudad.append(ciudad_nueva)
    return ciudad

def buscar_ciudad_por_identificacion(pasajeros, ciudad):
    identificacion = int(input("Ingrese la identificación del pasajero: "))
    for pasajero in pasajeros:
        if pasajero[1] == identificacion:
            destino = pasajero[2]
            for c in ciudad:
                if c[0].lower() == destino.lower():
                    return c[0]
            return "Ciudad no encontrada"
    return "Pasajero no encontrado"

def cantidad_pasajeros_a_ciudad(pasajeros, ciudad):
    nombre_ciudad = input("Ingrese el nombre de la ciudad: ")
    contador = 0
    for pasajero in pasajeros:
        if pasajero[2].lower() == nombre_ciudad.lower():
            contador += 1
    return contador

def buscar_pais_por_identificacion(pasajeros, ciudad):
    identificacion = int(input("Ingrese la identificación del pasajero: "))
    for pasajero in pasajeros:
        if pasajero[1] == identificacion:
            destino = pasajero[2]
            for c in ciudad:
                if c[0].lower() == destino.lower():
                    return c[1]
            return "País no encontrado"
    return "Pasajero no encontrado"

def cantidad_pasajeros_a_pais(pasajeros, ciudad):
    nombre_pais = input("Ingrese el nombre del país: ")
    contador = 0
    for pasajero in pasajeros:
        for c in ciudad:
            if c[0].lower() == pasajero[2].lower() and c[1].lower() == nombre_pais.lower():
                contador += 1
    return contador

pasajeros = [("Manuel Juárez", 19823451, "Armenia"),
             ("Gloria Galvis", 45789234, "Cali"),
             ("Rosa Ortiz", 45456234, "Medellín"),
             ("Eduardo Carrasquilla", 79844677, "Cali")]
ciudad = [("Armenia", "Quindío"),
          ("Cali", "Valle"),
          ("Medellin", "Antioquia")]

while True:
    print("1 agregar pasajeros")
    print("2 agregar ciudades")
    print("3 buscar ciudad destino por identificación")
    print("4 cantidad de pasajeros que viajan a una ciudad")
    print("5 buscar país destino mediante identificación")
    print("6 cantidad de pasajeros que viajan a un país")
    print("7 salir del programa")
    
    opcion = int(input("Acción a ejecutar: "))
    
    if opcion == 1:
        print("agregar pasajero")
        pasajeros = agregar_pasajeros(pasajeros)
    elif opcion == 2:
        print("agregar ciudad")
        ciudad = agregar_ciudades(ciudad)
    elif opcion == 3:
        print("buscar ciudad destino por identificación:")
        ciudad_destino = buscar_ciudad_por_identificacion(pasajeros, ciudad)
        print("el pasajero viaja a la ciudad de:", ciudad_destino)
    elif opcion == 4:
        print("la cantidad de pasajeros que viajan a una ciudad son:")
        cantidad = cantidad_pasajeros_a_ciudad(pasajeros, ciudad)
        print("La cantidad de pasajeros que viajan a esa ciudad es:", cantidad)
    elif opcion == 5:
        print("buscar el país del destino mediante identificación")
        pais_destino = buscar_pais_por_identificacion(pasajeros, ciudad)
        print("El pasajero viaja al país de", pais_destino)
    elif opcion == 6:
        print("l cantidad de pasajeros que viajan a un país son:")
        cantidad = cantidad_pasajeros_a_pais(pasajeros, ciudad)
        print("la cantidad de pasajeros que viajan a ese país son:", cantidad)
    elif opcion == 7:
        break
    else:
        print("opción inválida")

print("programa finalizado")"""

"""
import random

def obtener_opcion_usuario():
    while True:
        opcion = input("elige una opción (piedra, papel, tijera): ")
        if opcion.lower() in ["piedra", "papel", "tijera"]:
            return opcion.lower()
        else:
            print("opción inválida. Por favor, elige piedra, papel o tijera.")

def obtener_opcion_computadora():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

def determinar_ganador(opcion_usuario, opcion_computadora):
    if opcion_usuario == opcion_computadora:
        return "Empate"
    elif (
        (opcion_usuario == "piedra" and opcion_computadora == "tijera") or
        (opcion_usuario == "papel" and opcion_computadora == "piedra") or
        (opcion_usuario == "tijera" and opcion_computadora == "papel")
    ):
        return "gano"
    else:
        return "perdio :("

def jugar_piedra_papel_tijera():
    print("bienvenido a piedra, papel o tijera")
    while True:
        opcion_usuario = obtener_opcion_usuario()
        opcion_computadora = obtener_opcion_computadora()
        print("tu elección:", opcion_usuario)
        print("la elección de la computadora:", opcion_computadora)
        resultado = determinar_ganador(opcion_usuario, opcion_computadora)
        print(resultado)
        jugar_nuevamente = input("¿quieres jugar de nuevo? (s/n): ")
        if jugar_nuevamente.lower() != "s":
            break

jugar_piedra_papel_tijera()
"""
"""
def curso(nota):
    if nota < 5:
        return 'Mal'
    elif nota < 7:
        return 'Regular'
    elif nota < 9:
        return 'Bueno'
    elif nota < 10:
        return 'Muy bien'
    else:
        return 'Excelente'

def convertir_notas(diccionario_notas):
    diccionario_calificaciones = {}
    for asignatura, nota in diccionario_notas.items():
        calificacion = curso(nota)
        diccionario_calificaciones[asignatura.upper()] = calificacion
    return diccionario_calificaciones
notas = {
    'matemáticas': 8,
    'historia': 6,
    'ciencias': 9,
    'inglés': 7
}

calificaciones = convertir_notas(notas)
print(calificaciones)

{'matematicas': 'bueno', 'historia': 'regular', 'ciencias': 'muy bien', 'ingles': 'regular'}
"""