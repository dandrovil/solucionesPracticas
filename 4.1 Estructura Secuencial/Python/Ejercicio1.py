"""Un estudiante está cursando 5 materias, tiene la nota de cada materia y quiere saber cuál es su promedio.
Analisis:
    Entrada: nota1, nota2, nota3, nota4, nota5 tipoc flotante
    Proceso: sumanotas tipo flotante
             sumanotas = nota1 + nota2 + nota3 + nota4 + nota5
             promedio = sumanotas / 5
    Salida:  promedio tipo flotante
"""


nota1 = float(input("Ingrese la nota de la Materia N° 1: "))
nota2 = float(input("Ingrese la nota de la Materia N° 1: "))
nota3 = float(input("Ingrese la nota de la Materia N° 1: "))
nota4 = float(input("Ingrese la nota de la Materia N° 1: "))
nota5 = float(input("Ingrese la nota de la Materia N° 1: "))

sumanotas = nota1 + nota2 + nota3 + nota4 + nota5
promedio = float(sumanotas / 5)

print(" El promedio de las 5 materias es: ", promedio)

              