productos = {'8475HD':['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD':['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD':['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD':['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD':['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD':['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD':['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD':['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

editando_github=1


# productos = {modelo : [marca, pantalla, RAM, disco, GB de DD, procesador, video ...]}
# (DD)= Mecanico y (SSD)= Estado solido
stock = {'8475HD':[387990,10], 
'2175HD':[327990,4], 
'JjfFHD':[424990,1],
'fgdxFHD':[664990,21], 
'123FHD':[290890,32], 
'342FHD':[444990,7],
'GF75HD':[749990,2], 
'UWU131HD':[349990,1], 
'FS1230HD':[249990,0],
}
def stock_marca(): 
    marca = input('Ingrese marca a consultar: ').lower()
    encontrados = False
    for modelo, datos in productos.items():
        if datos[0].lower() == marca:
            print(f'Modelo: {modelo}, Marca: {datos[0]}, Stock: {stock.get(modelo, [0,0])[1]}')
            encontrados = True
    if not encontrados:
        print('No se encontró la marca ingresada.')
    
def busqueda_precio():
    p_min = int(input('Ingrese precio mínimo: '))
    p_max = int(input('Ingrese precio máximo: '))
    if p_max < p_min:
        print('El precio máximo debe ser mayor o igual al mínimo.')
        return
    encontrados = False
    for modelo, datos_stock in stock.items():
        precio = datos_stock[0]
        if p_min <= precio <= p_max:
            print(f'Modelo: {modelo}, Marca: {productos[modelo][0]}, Precio: {precio}, Stock: {datos_stock[1]}')
            encontrados = True
    if not encontrados:
        print('No hay modelos en ese rango de precios.')
            
def ordenar_productos():
    print('===Listado de notebooks===')
    for clave, valor in productos.items():
        print(f'{valor[0]} - {clave} - {valor[2]} - {valor[3]} - {valor[4]}')
        
def menu():
    while True:
        print('====================')
        print('***MENU PRINCIPAL***')
        print('====================')
        print('1. Stock marca.')
        print('2. Búsqueda por precio.')
        print('3. Listado de productos.')
        print('4. Salir.')
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            stock_marca()
        elif opcion == '2':
            busqueda_precio()
        elif opcion == '3':
            ordenar_productos()
        elif opcion == '4':
            print("Programa Finalizado!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# Menu principal
menu()