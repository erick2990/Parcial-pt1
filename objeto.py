from click import prompt

empleados = {}  # Diccionario vacío para guardar todos los empleados

class empleado:

    def __init__(self):
        informacion = {}

    def llenar_diccionario(self,codigo, nombre, dep, ant, punt, equipo, product, desemp, sat, telefono, correo):
        empleados[codigo] = {
            "nombre": nombre,
            "departamento": dep,
            "antiguedad": ant,
            "evaluacion": {
                "puntualidad": punt,
                "equipo": equipo,
                "productividad": product,
                "observaciones": desemp,
                "estado": sat
            },
            "contacto": {
                "telefono": telefono,
                "correo": correo
            }
        }

class manejo_ev(empleado):

    def calcular_promedio(self):
        print('El promedio del trabajador es: ')

class informacion_cont(empleado):

    def mostrar_informacion_cont(self):
        print('Informacion de contacto del trabajador')



def ingresar_empleados():
    print('Bienvenido!!!!')
    cantidad = int(input('Ingrese la cantidad de empleados que desea ingresar: '))
    for i in range(cantidad):
        print(f'\n\tIngrese los datos del trabajador {i + 1}:')
        codigo = input('Ingrese código único: ')
        nombre = input('Ingrese el nombre: ')
        dep = input('Ingrese el nombre del departamento: ')
        ant = input('Ingrese la antigüedad: ')
        punt = int(input('Calificación en puntualidad (0-10): '))
        equipo = int(input('Calificación en trabajo en equipo (0-10): '))
        product = int(input('Calificación en productividad (0-10): '))
        desemp = input('¿Ha tenido buen desempeño? (Sí/No): ')
        promedio = (punt + equipo + product) / 3
        sat = input('¿Desempeño satisfactorio? (S/N): ')
        telefono = input('Número de teléfono: ')
        correo = input('Correo electrónico: ')
        empleado_tmp = empleado(codigo, nombre, dep, ant, punt, equipo, product, desemp, promedio, sat, telefono, correo)




#funcion para mostrar los datos unicamente verifica antes si no hay empleados
def mostrarDatos():
    if not empleados:
        print("No hay empleados registrados.")
        return

    print("\nInformación de empleados:")
    for codigo, datos in empleados.items():
        print(f'\nCódigo: {codigo}')
        print(f'Nombre: {datos["nombre"]}')
        print(f'Departamento: {datos["departamento"]}')
        print(f'Antigüedad: {datos["antiguedad"]}')
        print(f'Teléfono: {datos["contacto"]["telefono"]}')
        print(f'Correo: {datos["contacto"]["correo"]}')
        print(f'Promedio de evaluación: {datos["evaluacion"]["promedio"]:.2f}')
        print(f'Estado: {"Satisfactorio" if datos["evaluacion"]["estado"].upper() == "S" else "No satisfactorio"}') #Verificaciond de estado del trabajador


# Menú principal
fin_menu = True

while fin_menu:
    try:
        print('\n\t\tBienvenido al sistema de gestión de trabajadores:')
        print('1. Ingresar datos de trabajador')
        print('2. Mostrar información')
        print('3. Calcular promedio y estado de evaluación (opcional)')
        print('4. Salir')
        opcion = int(input('Ingrese una opción: '))
        match opcion:
            case 1:
                ingresar_empleados()
            case 2:
                mostrarDatos()
            #case 3:

            case 4:
                print('Gracias por usar el sistema.')
                fin_menu = False
            case _:
                print('Opción incorrecta.')
    except Exception as e:
        print(f'Ocurrió un error: {e}. Vuelva a intentarlo.')
