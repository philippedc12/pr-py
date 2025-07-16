compras = {
    "Ana": [
        {"producto": "Leche", "cantidad": 2, "precio_unitario": 1000},
        {"producto": "Pan", "cantidad": 3, "precio_unitario": 800}
    ],
    "Luis": [
        {"producto": "Arroz", "cantidad": 1, "precio_unitario": 1500}
    ]
}

def mostrar_clientes():
    print("Clientes ingresados.")
    for cliente in compras:
        print(f"Clientes: {cliente}")
    
def ver_compras():
    nombre = input("Ingrese nombre de cliente para ver su compra: ")
    if nombre not in compras:
        print('Debe ingresar un nombre existente!')
        return
    print(f"Compras de {nombre}:")
    for compra in compras[nombre]:
        print(f"Producto: {compra['producto']}, Cantidad: {compra['cantidad']}, Precio unitario: {compra['precio_unitario']}")
        
def agregar_compra():
    nombre = input("Ingrese el nombre del cliente: ")
    if nombre not in compras:
        print("El cliente no existe. Use la opción para agregar un nuevo cliente.")
        return
    producto = input("Ingrese el producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = int(input("Ingrese el precio unitario: "))
    compras[nombre].append({"producto": producto, "cantidad": cantidad, "precio_unitario": precio})
    print("Compra agregada correctamente.")

def agregar_cliente():
    nombre = input("Ingrese el nombre del nuevo cliente: ")
    if nombre in compras:
        print("El cliente ya existe.")
        return
    producto = input("Ingrese el producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = int(input("Ingrese el precio unitario: "))
    compras[nombre] = [{"producto": producto, "cantidad": cantidad, "precio_unitario": precio}]
    print("Cliente y compra agregados correctamente.")
    
while True:
    print("\nMENU PRINCIPAL")
    print("1. Mostrar todos los clientes")
    print("2. Ver compras de un cliente")
    print("3. Agregar compra a cliente existente")
    print("4. Agregar nuevo cliente con su primera compra")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        mostrar_clientes()
    elif opcion == '2':
        ver_compras()
    elif opcion == '3':
        agregar_compra()
    elif opcion == '4':
        agregar_cliente()
    elif opcion == '5':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")