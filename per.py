# Lista para almacenar personas
personas = []

# CREATE
def crear_persona(nombre, edad):
    persona = {"nombre": nombre, "edad": edad}
    personas.append(persona)
    print(f"Persona {nombre} agregada.")

# READ
def mostrar_personas():
    if not personas:
        print("No hay personas registradas.")
    else:
        for i, persona in enumerate(personas):
            print(f"{i}. Nombre: {persona['nombre']}, Edad: {persona['edad']}")

# UPDATE
def actualizar_persona(indice, nuevo_nombre, nueva_edad):
    if 0 <= indice < len(personas):
        personas[indice]["nombre"] = nuevo_nombre
        personas[indice]["edad"] = nueva_edad
        print("Persona actualizada.")
    else:
        print("Índice inválido.")

# DELETE
def eliminar_persona(indice):
    if 0 <= indice < len(personas):
        persona = personas.pop(indice)
        print(f"Persona {persona['nombre']} eliminada.")
    else:
        print("Índice inválido.")

# Menú de ejemplo
while True:
    print("\n--- Menú CRUD ---")
    print("1. Crear persona")
    print("2. Mostrar personas")
    print("3. Actualizar persona")
    print("4. Eliminar persona")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        crear_persona(nombre, edad)
    elif opcion == "2":
        mostrar_personas()
    elif opcion == "3":
        mostrar_personas()
        indice = int(input("Índice a actualizar: "))
        nombre = input("Nuevo nombre: ")
        edad = int(input("Nueva edad: "))
        actualizar_persona(indice, nombre, edad)
    elif opcion == "4":
        mostrar_personas()
        indice = int(input("Índice a eliminar: "))
        eliminar_persona(indice)
    elif opcion == "5":
        break
    else:
        print("Opción inválida.")