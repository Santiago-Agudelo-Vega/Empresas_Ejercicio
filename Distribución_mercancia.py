#Una empresa dedicada a la distribucion de mercancia requiere el desarollo de un aplicativo que permita registrar los pedidos solicitados por los diferentes clientes
#dentro de los cuales se tiene la siguiente información: Nombre del cliente, direccion, contacto, sexo, descripcion de la casa, lugar de entrega
mi_diccionario = {}
import os
sw = True

def fnt_agregar(diccionario, Registro, Direccion, Contacto, Nombre, Sexo, DescC, Entrega):
    if Registro == '' or Direccion == '' or Contacto == '' or Nombre == '' or Sexo == '' or DescC == '' or Entrega == '':
        print('Debe diligenciar toda la información solicitada')
    else:
        diccionario[Direccion] = {'Nombre': Nombre, 'Dirección': Direccion, 'Contacto': Contacto, 'Sexo': Sexo, 'Descripcion de la casa': DescC, 'Entrega': Entrega}
        print(f'\nLa persona {Nombre} ha sido registrada con éxito')

def fnt_selector(op):
    if op == '1':
        os.system('cls')
        Nombre = input('Nombre:  ')
        Direccion = input('Direccion:  ')
        Contacto = input('Contacto:  ')
        Sexo = input('Sexo:  ')
        DescC = input('Descripcion de la casa: ')
        Entrega = input('Lugar de entrega: ')
        fnt_agregar(mi_diccionario, Direccion, Direccion, Contacto, Nombre, Sexo, DescC, Entrega)
        
while sw:
    os.system('cls')
    opcion = input('1. Registrar pedido\n2. Mostrar pedidos\n3. Salir\n- >  ')
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