boletas = [
   {"numero": 1001, "fecha": "01/08/2025", "cliente": "Juan Pérez", "total": 0},
   {"numero": 1002, "fecha": "02/08/2025", "cliente": "María López", "total": 0},
   {"numero": 1003, "fecha": "03/07/2025", "cliente": "Carlos Soto", "total": 0},
   {"numero": 1004, "fecha": "04/07/2025", "cliente": "Ana Torres", "total": 0},
   {"numero": 1005, "fecha": "05/07/2025", "cliente": "Pedro Rojas", "total": 0}, 
   {"numero": 1006, "fecha": "06/07/2025", "cliente": "Laura Díaz", "total": 0},
   {"numero": 1007, "fecha": "07/07/2025", "cliente": "Felipe Gutiérrez", "total": 0},
   {"numero": 1008, "fecha": "08/07/2025", "cliente": "Sofía Morales", "total": 0},
   {"numero": 1009, "fecha": "09/07/2025", "cliente": "Andrés Bravo", "total": 0},
   {"numero": 1010, "fecha": "10/07/2025", "cliente": "Gabriela Méndez", "total": 0},
]

detalle = [
# Boleta 1001
{"numero_boleta": 1001, "producto": "Leche", "cantidad": 2, "precio_unitario": 1200},
{"numero_boleta": 1001, "producto": "Pan", "cantidad": 1, "precio_unitario": 1500},
{"numero_boleta": 1001, "producto": "Huevos", "cantidad": 1, "precio_unitario": 2500},

# Boleta 1002
{"numero_boleta": 1002, "producto": "Arroz", "cantidad": 1, "precio_unitario": 1800},
{"numero_boleta": 1002, "producto": "Fideos", "cantidad": 2, "precio_unitario": 900},

# Boleta 1003
{"numero_boleta": 1003, "producto": "Aceite", "cantidad": 1, "precio_unitario": 3000},
{"numero_boleta": 1003, "producto": "Azúcar", "cantidad": 1, "precio_unitario": 1500},
{"numero_boleta": 1003, "producto": "Café", "cantidad": 1, "precio_unitario": 2500},

# Boleta 1004
{"numero_boleta": 1004, "producto": "Pan", "cantidad": 2, "precio_unitario": 1500},
{"numero_boleta": 1004, "producto": "Sal", "cantidad": 1, "precio_unitario": 800},

# Boleta 1005
{"numero_boleta": 1005, "producto": "Jugo", "cantidad": 2, "precio_unitario": 1200},
{"numero_boleta": 1005, "producto": "Leche", "cantidad": 1, "precio_unitario": 1200},
{"numero_boleta": 1005, "producto": "Arroz", "cantidad": 1, "precio_unitario": 1800},

# Boleta 1006
{"numero_boleta": 1006, "producto": "Huevos", "cantidad": 1, "precio_unitario": 2500},
{"numero_boleta": 1006, "producto": "Café", "cantidad": 1, "precio_unitario": 2500},

# Boleta 1007
{"numero_boleta": 1007, "producto": "Azúcar", "cantidad": 1, "precio_unitario": 1500},
{"numero_boleta": 1007, "producto": "Fideos", "cantidad": 2, "precio_unitario": 900},

# Boleta 1008
{"numero_boleta": 1008, "producto": "Pan", "cantidad": 1, "precio_unitario": 1500},
{"numero_boleta": 1008, "producto": "Sal", "cantidad": 1, "precio_unitario": 800},
{"numero_boleta": 1008, "producto": "Aceite", "cantidad": 1, "precio_unitario": 3000},
{"numero_boleta": 1008, "producto": "Jugo", "cantidad": 1, "precio_unitario": 1200},

# Boleta 1009
{"numero_boleta": 1009, "producto": "Leche", "cantidad": 2, "precio_unitario": 1200},
{"numero_boleta": 1009, "producto": "Huevos", "cantidad": 1, "precio_unitario": 2500},
{"numero_boleta": 1009, "producto": "Arroz", "cantidad": 1, "precio_unitario": 1800},

# Boleta 1010
{"numero_boleta": 1010, "producto": "Fideos", "cantidad": 2, "precio_unitario": 900},
{"numero_boleta": 1010, "producto": "Café", "cantidad": 1, "precio_unitario": 2500},
]

def muestra_boleta(bol):
    if bol==None:
        print('La boleta no existe!')
        return
    print('Datos Boleta:') 
    print("====================================")
    print('Numero: ',bol["numero"])
    print('Fecha: ',bol["fecha"])
    print('Cliente: ',bol["cliente"])
    print('Total: ',bol["total"])
    print("====================================")
    print('Producto\tCantidad\tPrecio Unitario\tSubtotal')
    for det in detalle:
        if det["numero_boleta"]==bol["numero"]:
            subtotal=det["cantidad"]*det["precio_unitario"]
            print(f'{det["producto"]}\t\t{det["cantidad"]}\t\t{det["precio_unitario"]}\t\t{subtotal}')

productos=["Leche","Huevos","Arroz","Cafe","Fideos","Aceite","Jugo","Azucar"]         
                
# {"numero_boleta": 1009, "producto": "Leche", "cantidad": 2, "precio_unitario": 1200},


def buscar_boleta(num_boleta):
    for bol in boletas:
        if bol["numero"]==num_boleta:
            return(bol)
    return None

def actualiza_totales():
    for bol in boletas:
        total=0
        for det in detalle:
            if det["numero_boleta"]==bol["numero"]:
                total+=det["cantidad"]*det["precio_unitario"]
        bol["total"]=total
        

def totales(mes,annio):
    total=0
    for bol in boletas:       
        fecha=bol["fecha"].split('/') #dd/mm/yyyy
    if int(fecha[1])==mes and int(fecha[2])==annio:
        for det in detalle:
            if det["numero_boleta"]==bol["numero"]:
                total+=det["cantidad"]*det["precio_unitario"]
    print(f'El total del mes {mes} y año {annio} es igual a {total}')


def agrega_productos(numero_boleta):
    bol=buscar_boleta(numero_boleta)
    if bol==None:
        print('Boleta no existe')
        return
    while True:
        nom=input('Ingrese Nombre del Producto:').capitalize()
        if nom in productos:
            break
        else:
            print('El producto no existe!')
    while True:
        try:
            cant=int(input('Ingrese cantidad del producto: '))
            break
        except:
            print('Cantidad debe ser un numero entero!')
    while True:
        try:
            precio_unitario=int(input('Ingrese precio unitario del producto: '))
            break
        except:
            print('Cantidad debe ser un numero entero!')
        detalle.append({"numero_boleta":numero_boleta, "producto":productos , "cantidad":cant, "precio_unitario":precio_unitario})
        
while True:
    print("MENÚ PRINCIPAL SUPERMERCADO DUMBO")
    print("====================================")
    print('1. Total vendido en un mes y año en particular.')
    print('2. Información de una boleta específica, incluyendo su detalle.')
    print('3. Agregar uno o más productos a una boleta.')
    print('4. Actualizar el total de todas las boletas.')
    print('5. Salir.')
    opc=input('Ingrese Opcion: ')
    if opc=='1':
        totales(8,2025)
    elif opc=='2':
        b=buscar_boleta(1001)
        muestra_boleta(b)
    elif opc=='3':
        agrega_productos(1001)
    elif opc=='4':
        actualiza_totales()
    elif opc=='5':
        print('Gracias por preferirnos!')
        break
    else:
        print('Ingrese una opcion valida!')        
