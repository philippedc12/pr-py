vehiculos = {
    "ABCD12": ["Toyota", "Corolla", 2020, "Sedán"],
    "EFGH34": ["Hyundai", "Tucson", 2022, "SUV"],
    "IJKL56": ["Chevrolet", "Spark", 2019, "Hatchback"],
    "MNOP78": ["Kia", "Rio", 2021, "Sedán"],
    "QRST90": ["Ford", "Escape", 2020, "SUV"],
    "UVWX11": ["Nissan", "Versa", 2018, "Sedán"],
    "YZAB22": ["Honda", "Civic", 2023, "Sedán"],
    "CDEF33": ["Mazda", "CX-5", 2022, "SUV"],
    "GHIJ44": ["Peugeot", "208", 2021, "Hatchback"],
    "KLMN55": ["Volkswagen", "Golf", 2020, "Hatchback"]
}

mantenciones = {

 10: {"patente": "ABCD12", "costo_total": 180000, "repuestos": ["Filtro de aceite", "Aceite", "Bujías"], "fecha": "05/01/2025"},
 20: {"patente": "EFGH34", "costo_total": 250000, "repuestos": ["Pastillas de freno", "Aceite", "Filtro aire"], "fecha": "12/01/2025"},
 30: {"patente": "IJKL56", "costo_total": 160000, "repuestos": ["Aceite", "Batería"], "fecha": "25/01/2025"},
 40: {"patente": "MNOP78", "costo_total": 195000, "repuestos": ["Filtro de aceite", "Aceite", "Correa distribución"], "fecha": "04/02/2025"},
 50: {"patente": "QRST90", "costo_total": 220000, "repuestos": ["Amortiguadores", "Filtro aire"], "fecha": "18/02/2025"},
 60: {"patente": "UVWX11", "costo_total": 175000, "repuestos": ["Bujías", "Aceite", "Filtro de combustible"], "fecha": "01/03/2025"},
 70: {"patente": "YZAB22", "costo_total": 280000, "repuestos": ["Pastillas de freno", "Aceite", "Radiador"], "fecha": "11/03/2025"},
 80: {"patente": "CDEF33", "costo_total": 240000, "repuestos": ["Aceite", "Filtro aceite", "Filtro aire"], "fecha": "20/03/2025"},
 90: {"patente": "GHIJ44", "costo_total": 170000, "repuestos": ["Aceite", "Bujías"], "fecha": "02/04/2025"},
 100: {"patente": "KLMN55", "costo_total": 200000, "repuestos": ["Correa distribución", "Aceite", "Filtro aceite"], "fecha": "14/04/2025"},
 110: {"patente": "ABCD12", "costo_total": 150000, "repuestos": ["Aceite", "Filtro aire"], "fecha": "29/04/2025"},
 120: {"patente": "EFGH34", "costo_total": 230000, "repuestos": ["Aceite", "Radiador"], "fecha": "05/05/2025"},
 130: {"patente": "IJKL56", "costo_total": 165000, "repuestos": ["Filtro aceite"], "fecha": "19/05/2025"},
 140: {"patente": "YZAB22", "costo_total": 190000, "repuestos": [], "fecha": "01/06/2025"},
 150: {"patente": "CDEF33", "costo_total": 210000, "repuestos": ["Bujías", "Aceite"], "fecha": "10/06/2025"},
 160: {"patente": "EFGH34", "costo_total": 245000, "repuestos": ["Aceite", "Bujías", "Filtro aceite"], "fecha": "22/06/2025"},
 170: {"patente": "GHIJ44", "costo_total": 180000, "repuestos": [], "fecha": "29/06/2025"},
 180: {"patente": "ABCD12", "costo_total": 155000, "repuestos": ["Aceite", "Filtro combustible"], "fecha": "30/06/2025"},
 190: {"patente": "MNOP78", "costo_total": 190000, "repuestos": ["Aceite", "Filtro aceite", "Filtro aire"], "fecha": "28/06/2025"},
 200: {"patente": "UVWX11", "costo_total": 170000, "repuestos": ["Correa distribución", "Aceite"], "fecha": "27/06/2025"}
}

marcas=['Mazda', 'Chevrolet', 'Ford', 'Hyundai', 'Peugeot', 'Nissan', 'Kia', 'Volkswagen', 'Honda', 'Toyota']

# Funciones
def muestra_vehiculo(patente):
    vehic=buscar_vehiculo(patente)
    if vehic!=None:
        for patente,lista in vehic.items():
            print('Datos de Vehiculo')
            print('==================')
            print('Patente: ',patente)
            print('Marca: ',lista[0])
            print('Modelo: ',lista[1])
            print('Año Fab: ',lista[2])
            print('Tipo: ',lista[3])
            print('Costo\tFecha\t\tRepuestos')
            tiene_mantenciones=False
            for cod, datos in mantenciones.items():
                if datos["patente"] == patente:
                    tiene_mantenciones=True
                    print(f'{datos["costo_total"]}\t{datos["fecha"]}\t{datos["repuestos"]}')
                if not tiene_mantenciones:
                    print('El Vehiculo no tiene mantenciones!')
    else:
        print('Vehiculo no existe!')
        
    # "KLMN55": ["Volkswagen", "Golf", 2020, "Hatchback"]
    
def buscar_vehiculo(patente):
    veh={}
    if patente in vehiculos:
        veh[patente]=(vehiculos[patente])
        return(veh)
    else:
        return None

def total_mantenciones(pat):
    vehic=buscar_vehiculo(pat)
    if vehic!=None:
        for patente,lista in vehic.items():
            print('==================')
            print('Datos de Vehiculo')
            print('==================')
            print('Patente:',patente)
            print('Marca:',lista[0])
            print('Modelo:',lista[1])
            print('Año Fab:',lista[2])
            print('Tipo:',lista[3])
            total=0
            for cod, datos in mantenciones.items():
                if datos["patente"] == patente:
                    total=total+datos["costo_total"]
            print('Total mantenciones $:',total)
    else:
        print('Vehiculo no existe!')
def total_repuestos(nom_rep):
    contador=0
    for clave,valor in mantenciones.items():
        if nom_rep in valor["repuestos"]:
            contador+=1
    print(f'El total de repuestos de ({nom_rep}) es:',contador)
        
# programa principal
def nuevo_vehiculo(vehiculos):
    patente=input('Ingrese la patente: ')
    if patente in vehiculos:
        print('La patente ya existe!')
        return
    # Validar 4 letras 2 digitos  
    while True:
        marca=input('Ingrese marca:: ').capitalize()
        if marca not in marcas:
            print('Marca no existe en marcas!')
        else:
            break
    modelo=input('Ingrese modelo: ').capitalize()
    while True:
        try:
            annio=int(input('Ingrese Año de fabricacion: '))
            if annio>=1980 and annio<=2025:
                break
        except:
            print('Año incorrecto!')
    tipo=input('Ingrese tipo de Vehiculo: ').capitalize()
    vehiculos[patente]=[marca,modelo,annio,tipo]
              
#  "YZAB22": ["Honda", "Civic", 2023, "Sedán"]    
    
opc='8'
while opc!='5':
    print('MENU PRINCIPAL TALLER MECANICO')
    print('==============================')
    print('1. Total en $ de todas las mantenciones de un vehiculo especifico.')
    print('2. Informacionn de un vehiculo especifico y sus mantenciones.')
    print('3. Cantidad total de repues1tos X utilizados.')
    print('4. Ingresar un nuevo vehiculo (no se puede repetir la patente).')
    print('5. Salir.')
    opc=input('Ingrese una opcion: ')
    pat="MNOP78"
    if opc=='1':
        total_mantenciones(pat)
    elif opc=='2':
        muestra_vehiculo(pat)
    elif opc=='3':
        total_repuestos(mantenciones)
    elif opc=='4':
        nuevo_vehiculo(vehiculos)
    elif opc=='5':
        print('Gracias por preferirnos!')
    else:
        print('Ingrese una opcion valida!')