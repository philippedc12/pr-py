meeee# Diccionario original de turistas
turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"]
}

# Función Opción 1: Turistas por país
def turistas_por_pais(pais):
    encontrados = [info[0] for info in turistas.values() if info[1].lower() == pais.lower()]
    if encontrados:
        print("\nTuristas de", pais + ":")
        for nombre in encontrados:
            print("-", nombre)
    else:
        print("\nNo se encontraron turistas de", pais)

# Función Opción 2: Turistas por mes
def turistas_por_mes(mes):
    total = len(turistas)
    conteo = 0
    for datos in turistas.values():
        fecha = datos[2]
        mes_turista = int(fecha.split("-")[1])
        if mes_turista == mes:
            conteo += 1
    if total > 0:
        porcentaje = round((conteo / total) * 100, 1)
    else:
        porcentaje = 0
    return porcentaje

# Función Opción 3: Eliminar turista
def eliminar_turista():
    nombre = input("Ingrese el nombre del turista que desea eliminar: ").strip().lower()
    encontrado = False
    for key in list(turistas.keys()):
        if turistas[key][0].lower() == nombre:
            del turistas[key]
            encontrado = True
            print("Turista eliminado con éxito.")
            break
    if not encontrado:
        print("Turista no encontrado. No se pudo eliminar.")

# Función principal con menú
def main():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1.- Turistas por país.")
        print("2.- Turista por mes.")
        print("3.- Eliminar turista.")
        print("4.- Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pais = input("Ingrese el país de origen: ")
            turistas_por_pais(pais)

        elif opcion == "2":
            while True:
                try:
                    mes = int(input("Ingrese el número del mes (1 al 12): "))
                    if 1 <= mes <= 12:
                        porcentaje = turistas_por_mes(mes)
                        print(f"Porcentaje de turistas que ingresaron en el mes {mes}: {porcentaje}%")
                        break
                    else:
                        print("Debe ingresar un número entre 1 y 12.")
                except ValueError:
                    print("Entrada inválida. Debe ingresar un número.")

        elif opcion == "3":
            eliminar_turista()

        elif opcion == "4":
            print("Programa terminado...")
            break

        else:
            print("Debe seleccionar una opción válida.")

# Ejecutar programa
main()
