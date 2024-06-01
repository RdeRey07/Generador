#1. Escriba una función redondear() que permita redondear un número
#decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
#entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
#anterior (3). 

def redondear(numero):
    if numero > 3.50:
        return int(numero) + 1
    else:
        return int(numero)

print(redondear(3.51))  
print(redondear(3.50))  
print(redondear(3.49))  

