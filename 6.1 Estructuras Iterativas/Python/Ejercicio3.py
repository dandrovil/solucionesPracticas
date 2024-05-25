"""Pedir que el usuario ingrese (input) nombre de personas y mostrarlos hasta que el valor de lo que ingresa sea “fin”

Analisis:
            Entrada: nombre tipo cadena
            Proceso: Iteracion infinita + Condicional (nombre = "fin")
            Salida:  nombre tipo cadena
"""

while True:
    nombre = input("Ingrese un nombre (fin para terminar): ")
    if nombre.lower() == "fin":
        break
    print("El nombre ingresado es: ", nombre)
