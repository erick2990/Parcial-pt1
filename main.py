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
        codigo = input('Ingres codigo unico: ')
        nombre = input('Ingrese el nombre; ')
        dep = input('Ingrese el nombre del departamento: ')
        ant = input('Ingrese la antiguedad: ')
        punt = int(input('Ingrese una calificacion de  0 a 10 en puntualidad'))
        equipo = int(input('Ingrese una calificacion de  0 a 10 en puntualidad'))
        product = int(input('Ingrese una calificacion de  0 a 10 en puntualidad'))
        desemp = input('Ingrese si ha tenido un buen desempeño: ')
        promedio = (equipo + product + punt) /3
        sat = input('Ingrese si ha tenido un desempeño satisfactorio o no (S/N)')
        telefono = input('Ingrese numero de telefono: ')
        correo = input('Ingrese el correo: ')
        empleados = {
            "codigo":{
                "nombre" : nombre,
                "departamento" : dep,
                "antiguedad" : ant,
                "evaluacion" : {
                    "puntualidad" : punt,
                    "equipo": equipo,
                    "productividad": product,
                    "observaciones": desemp,
                    "promedio" : promedio,
                    "Estado" : sat
                }
            },
            "contacto":{
                "telefono" : telefono,
                "correo" : correo
            }
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

    except Exception as e:
        print('Ocurrio un error vuelva  a intentarlo')





