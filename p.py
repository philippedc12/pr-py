productos=[]

def agregar_producto(productos):
    producto = input('Ingrese el producto que desea: ').lower()
    productos.append(producto)
    print('Producto agregado:', producto)
        
def eliminar_producto(productos):
    eliminar=input('Ingrese el producto que desea eliminar: ')
    if eliminar in len(productos):
        print('Producto eliminado correctamente!') 
    else:
        print('El producto no existe!')  
def mostrar_productos(productos):
    if not productos:
        print("No hay productos registrados.")
    else:
        for i, producto in enumerate(producto):
            print(f"{i}. 1. {producto}")

while True:
    print('Lista de Compras')
    print('===========')
    print('1. Agregar producto')
    print('2. Eliminar producto')
    print('3. Ver lista')
    print('4. Buscar producto')
    print('5. Salir')     
    opc=input('Seleccione una opcion: ')
    if opc=='1':
        agregar_producto(productos)
    elif opc=='2':
        print('opc2')
    elif opc=='3':
        mostrar_productos(productos)
    elif opc=='4':
        print('opc4')
    elif opc=='5':
        print('Gracias por tu atencion!')
        break
    else:
        print('Ingresa una opcion valida!')