mascotas = {
            }

from datetime import datetime

def ingresar_mascota():
    nombre = input('Ingrese nombre de su mascota: ').capitalize()
    tipo_mascota = input('Ingrese P para Perro, G para Gato, A para Ave: ').upper()
    fecha_str = input('Ingrese Fecha de registro en DD-MM-AAAA: ')
    try:
        fecha_registro = datetime.strptime(fecha_str, '%d-%m-%Y')
    except ValueError:
        print('Formato de fecha incorrecto. Debe ser DD-MM-AAAA.')
        return
    edad = int(input('Ingrese Edad de su mascota: '))
    if nombre in mascotas:
        print('Debe ingresar un nombre nuevo!')
        return
    if tipo_mascota not in ['P', 'G', 'A']:
        print('Debe ingresar solo P, G o A!')
        return
    # Aquí puedes guardar la mascota si todo es correcto
    mascotas[nombre] = {
        'tipo': tipo_mascota,
        'fecha_registro': fecha_registro.strftime('%d-%m-%Y'),
        'edad': edad
    }
    print('Mascota registrada correctamente!')

def buscar_mascota():
    buscar = input('Ingrese el nombre de mascota que desea buscar: ').capitalize()
    if buscar in mascotas:
        print('Busqueda exitosa!')
        print('Tipo de mascota:', mascotas[buscar]["tipo"])
        print('Fecha:', mascotas[buscar]["fecha_registro"])
        print('Edad:', mascotas[buscar]["edad"])
    else:
        print('Mascota no encontrada!')
    
def eliminar_mascota():
    eliminar = input('Ingrese el nombre de mascota para eliminar: ').capitalize()
    if eliminar in mascotas:
        del mascotas[eliminar]
        print('Mascota eliminada!')
    else:
        print('No se pudo eliminar la mascota')

def mascotas_registro():
    annio = input('Ingrese el año para mostrar registro: ')
    encontrados = False
    for nombre, datos in mascotas.items():
        # Extraer el año de la fecha de registro
        if datos['fecha_registro'][-4:] == annio:
            print(f"Nombre: {nombre}, Tipo: {datos['tipo']}, Fecha: {datos['fecha_registro']}, Edad: {datos['edad']}")
            encontrados = True
    if not encontrados:
        print('No hay mascotas registradas en ese año.')
        
while True:
    print('=================')
    print('MENU DE MASCOTAS')
    print('=================')
    print('1. Ingresar mascotas.')
    print('2. Buscar mascotas.')
    print('3. Eliminar mascota.')
    print('4. Buscar por año de registro.')
    print('5. Salir.')
    opc = input('Ingrese una opcion: ')
    if opc=='1':
        ingresar_mascota()
    elif opc=='2':
        buscar_mascota()
    elif opc=='3':
        eliminar_mascota()
    elif opc=='4':
        mascotas_registro()
    elif opc=='5':
        print('Gracias por preferirnos!')
        break
    else:
        print('Ingrese una opcion valida!')
            