#Ejercicio 1: Una transportadora requiere el desarollo de una aplicación que permita llevar un registro de los despachos de sus vehiculos teniendo en cuenta lo siguiente:
#1 placa del vehiculo 2 descripcion del vehiculo 3 nombre del conductor 4 contacto del conductor 5 ruta 6 y descripcion de la carga el numero de despacho se genera de manera automatica.
#dicha informacion debe quedar registrada en un diccionario. el sistema debe realizar: registro de salidas y mostrar salidas 

mi_diccionario = {}
import os
sw = True

def fnt_agregar(diccionario, Registro, PlacaV, DescV, Nombre, ContactoC, Ruta, Carga):
    if Registro == '' or PlacaV == '' or DescV == '' or Nombre == '' or ContactoC == '' or Ruta == '' or Carga == '':
        print('Debe diligenciar toda la información solicitada')
    else:
        diccionario[PlacaV] = {'Nombre': Nombre, 'Placa del vehiculo': PlacaV, 'Descripcion del vehiculo': DescV, 'Contacto del conductor': ContactoC, 'Ruta del conductor': Ruta, 'Carga': Carga}
        print(f'\nLa persona {Nombre} ha sido registrada con éxito')

def fnt_selector(op):
    if op == '1':
        os.system('cls')
        Nombre = input('Nombre:  ')
        PlacaV = input('Placa del vehiculo:  ')
        DescV = input('Descripción del vehiculo:  ')
        ContactoC = input('Contacto del conductor:  ')
        Ruta = input('Ruta: ')
        Carga = input('Carga: ')
        fnt_agregar(mi_diccionario, PlacaV, PlacaV, DescV, Nombre, ContactoC, Ruta, Carga)
        
while sw:
    os.system('cls')
    opcion = input('1. Registro de Salidas\n2. Mostrar Salidas\n3. Salir\n- >  ')
    if opcion == '1':
        fnt_selector(opcion)
    elif opcion == '2':
        os.system('cls')
        print('\nCantidad de registros: ',len(mi_diccionario),'\n')
        for clave, valor in mi_diccionario.items():
            print(f"{clave}: {valor}")
        input('\n\nPresione ENTER para continuar...')
    elif opcion == '3':
        sw = False