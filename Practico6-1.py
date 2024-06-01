
import time

inicio = time.time()




#2. Coloque el módulo del ejercicio anterior dentro de un paquete. En un
#módulo que esté fuera de ese paquete, cree una función de suma de
#decimales que redondee el resultado haciendo uso de la función
#redondear() del paquete recién creado.

from Practico6 import redondear

def suma_redondeada(a, b):
    resultado = a + b
    return redondear(resultado)

if __name__ == "__main__":
    print(suma_redondeada(1.25, 2.30))  # Debería imprimir 3
    print(suma_redondeada(1.75, 2.10))  # Debería imprimir 4

#3. Usando el módulo datetime, escribe un programa que muestre la fecha
#y hora actuales del sistema.

from datetime import datetime

def mostrar_fecha_hora_actual():
    fecha_hora_actual = datetime.now()
    fecha_formateada = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")
    print("Fecha y hora actuales:", fecha_formateada)

mostrar_fecha_hora_actual()

#4. Escriba un programa que devuelva un número par al azar entre 2 y 10
#(pista: para comprobar si se pueden generar todos los números, pruebe
#ejecutar el programa dentro de un ciclo infinito).

import random

def generar_par_azar():
    return random.choice([2, 4, 6, 8, 10])

def main():
    print("Generador de números pares al azar entre 2 y 10")
    print("Escribe 'salir' para terminar el programa.")

    while True:
        comando = input("Presiona Enter para generar un número par (o escribe 'salir' para terminar): ")
        if comando.lower() == "salir":
            print("Programa terminado. ¡Hasta luego!")
            break
        else:
            numero_par = generar_par_azar()
            print("Número par generado:", numero_par)

if __name__ == "__main__":
    main()


import random

def bola_magica():
    respuestas = [
        "Es seguro que sí",
        "Las chances son buenas",
        "Puedes contar con ello",
        "Pregúntame de nuevo más tarde",
        "Concéntrate y pregunta de nuevo",
        "No veo con claridad, intenta de nuevo",
        "Mi respuesta es no",
        "Mis fuentes me dicen que no"
    ]
    return random.choice(respuestas)

while True:
    pregunta = input("Haz tu pregunta a la Bola Mágica (o escribe 'salir' para terminar): ")
    if pregunta.lower() == "salir":
        print("Gracias por jugar con la Bola Mágica. ¡Hasta luego!")
        break
    else:
        print("La Bola Mágica dice:", bola_magica())

#6. Encuentre el tiempo de ejecución de los programas de los ejercicios
#anteriores (pista: use el módulo time)


fin = time.time()

tiempo_ejecucion = fin - inicio

print("El tiempo de ejecución fue de:", tiempo_ejecucion, "segundos")

#7. (Opcional) Sorteo: Escriba un programa que simule un sorteo donde
#toman uno o más papeles al azar de un pozo para elegir los ganadores.

def sorteo(participantes, ganadores):
    if participantes < ganadores:
        print("No hay suficientes participantes para elegir esa cantidad de ganadores.")
        return

    lista_participantes = list(range(1, participantes + 1))

    ganadores_sorteo = random.sample(lista_participantes, ganadores)

    print("Los ganadores del sorteo son:")
    for i, ganador in enumerate(ganadores_sorteo):
        print("Ganador {}: {}".format(i + 1, ganador))

try:
    num_participantes = int(input("Ingrese la cantidad de participantes: "))
    num_ganadores = int(input("Ingrese la cantidad de ganadores a elegir: "))
except ValueError:
    print("Por favor, ingrese un número válido.")
    exit()

sorteo(num_participantes, num_ganadores)
