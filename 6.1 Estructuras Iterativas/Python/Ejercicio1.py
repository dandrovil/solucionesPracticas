"""Mostrar los números desde el 0 al número solicitado al usuario (input)

Analisis:
            Entrada: numero tipo entero
            Proceso: i tipo entero
                     Iteracion de 1 hasta numero + 1 
            Salida:  i tipo entero
"""


numero = int(input("Ingrese un numero: "))
for i in range(numero + 1):
    print(i)
