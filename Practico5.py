#) Hacer un programa que gestiones datos para una escuela.
#El programa tiene que ser capaz de:
#a) Llevar un registro de todos los datos de alumnos de la escuela (Nombre,
#Apellido, fecha de nacimiento, DNI, Nombre de Tutor, registro de todas las
#notas, cantidad de faltas, cantidad de amonestaciones recibidas.
#b) Mostrar los datos de cada alumno
#c) Modificar los datos de los alumnos
#d) Agregar alumnos
#e) Expulsar alumnos



datos = {
    "Alumnos": []
}

def agregación():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    fecharda = input("Fecha de nacimiento: ")
    tutor = input("Nombre y apellido del tutor: ")
    notas = []
    faltas = 0
    amonestaciones = 0
    
    alumno = {
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "Fecha de nacimiento": fecharda,
        "Tutor": tutor,
        "Notas": notas,
        "Faltas": faltas,
        "Amonestaciones": amonestaciones
    }
    
    datos["Alumnos"].append(alumno)
    print("Alumno agregado exitosamente.")

def listarada_Dea():
    for i, alumno in enumerate(datos["Alumnos"]):
        print(f"\nAlumno {i+1}:")
        for key, value in alumno.items():
            print(f"{key}: {value}")

def modificador():
    dni = input("Ingrese el DNI del alumno a modificar: ")
    for alumno in datos["Alumnos"]:
        if alumno["DNI"] == dni:
            print("Alumno encontrado. Ingrese los nuevos datos:")
            alumno["Nombre"] = input("Nombre: ")
            alumno["Apellido"] = input("Apellido: ")
            alumno["Fecha de nacimiento"] = input("Fecha de nacimiento: ")
            alumno["Tutor"] = input("Nombre y apellido del tutor: ")
            alumno["Notas"] = list(map(int, input("Notas (separadas por coma): ").split(',')))
            alumno["Faltas"] = int(input("Cantidad de faltas: "))
            alumno["Amonestaciones"] = int(input("Cantidad de amonestaciones: "))
            print("Datos del alumno actualizados.")
            return
    print("Alumno no encontrado.")


def Expulsión():
    dni = input("Ingrese el DNI del alumno a expulsar: ")
    for i, alumno in enumerate(datos["Alumnos"]):
        if alumno["DNI"] == dni:
            del datos["Alumnos"][i]
            print("Alumno expulsado exitosamente.")
            return
    print("Alumno no encontrado.")

def Alumnado():
    while True:
        print("\nGestión de datos de la escuela")
        print("1. Agregar alumno")
        print("2. Mostrar datos de los alumnos")
        print("3. Modificar datos de un alumno")
        print("4. Expulsar alumno")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregación()
        elif opcion == '2':
            listarada_Dea()
        elif opcion == '3':
            modificador()
        elif opcion == '4':
            Expulsión()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

Alumnado()
