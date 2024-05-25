"""Mostrar sólo los números pares desde 0 hasta el número ingresado (input). Nota: para saber si un número es par hacer i % 2 == 0)

Analisis:
            Entrada: numero tipo entero
            Proceso: i tipo entero
                     Iteracion de 1 hasta numero + 1
                     Condiconal (i % 2 == 0)
            Salida:  i tipo entero
"""

numero = int(input("Ingrese un numero: "))
for i in range(numero + 1):
    if i % 2 == 0:
        print(i)
