from cloudinit.sources.DataSourceVMware import exec_vmware_rpctool

empleados = {} #Diccionario vacio para guardar todos los empleados


class empleado:

   def __init__(self):
       informacion_general ={}


def ingresar_empleados():
    print('Bienvenido!!!!')
    cantidad = int(input('Ingrese cuantos empleados desea agregar: '))
    for i in range(0, cantidad):
        print(f'\t\t\tIngrese los datos del {i+1} trabajador: ')
        empleados["codigo"] = input('Ingres codigo unico: ')
        empleados["codigo"] = {
            "nombre"= input('Ingrese el nombre: ')
            empleados["departamento"] = input('Ingrese el departamento: ')
            empleados["antig"] = input('Ingrese cuantos anios ha laborado el trabjaador: ')
            empleado_tmp = empleado()  # Se instancia el objeto de tipo empleado para acceeder a sus subdiccionario
        }



fin_menu =True


while fin_menu:

    try:
        print('\r\t\tBienvenido al sistema de gestion de trabajadores:')
        print('1. Ingresar datos de trabajador\n2.Mostrar informacion \n3.Calcular promedio y estado de evaluacion')
        print('4.Salir')
        opcion = int(input('Ingrese una opcion: '))
        match opcion:
            case 1:
                ingresar_empleados()
            #case 2:

            #case 3:

            case 4:
                print('Gracias por usar el sistema')
                fin_menu = False
            case _:
                print('Opcion incorrecta')

    except ValueError:
        print('Ocurrio un error vuelva  a intentarlo')





