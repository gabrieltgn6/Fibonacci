

# Programa para calcular fibonacci a partir de un numero dado

datos = int(input("Que numero quieres calcular?"))

a = 0
b = 1

for i in range (datos):

    a = b
    b = a + b    


print = b

"""

datos = int(input("¿Qué número quieres calcular en la serie de Fibonacci? "))

# Inicializamos las variables de la serie de Fibonacci
a, b = 0, 1

# Mostramos los primeros "datos" números de la serie de Fibonacci
for i in range(datos):
    print(a, end=" ")

    # Calculamos el siguiente número en la serie
    a, b = b, a + b
"""