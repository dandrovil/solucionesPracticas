"""En una escuela, luego de tomar un determinado examen, es necesario calcular el promedio de notas (las notas van de 0 a 10) de los alumnos de un curso. 
Se necesita saber si el rendimiento ha sido elevado (el promedio es mayor a 8), aceptable (el promedio está comprendido entre 6 y 8) o bajo (promedio es inferior a 6).
Desarrollar un algoritmo que resuelva este problema. Para tener en cuenta: las autoridades del colegio saben cuántos estudiantes del curso han rendido el examen.

Analisis:
            Entrada: cant_est tipo entero 
                     nota tipo flotante
            Proceso: promedio como flotante
                     iteracion (i hasta cant_est)
                     Iteracion (nota<0 o nota>10)
                     promedio = promedio + nota
                     promedio = promedio / cant_est
                     Condicional (promedio >=6 y promedio <= 8)
                     Condicional (promedio > 8) 
            Salida:  Promedio como flotante
                     Mensaje como cadena

"""
cant_est = int(input("Ingrese la cantidad de estudiantes que rindieron el examen: "))
promedio = 0.0
for i in range(cant_est):
    nota = float(input(f"Ingrese la nota del estudiante Nº {i+1}: "))
    while nota < 0 or nota > 10:
        nota =float(input("ERROR nota invalida, ingrese un valor entre 0 y 10: "))
    promedio = promedio + nota
promedio = promedio / cant_est
print(f"El promedio total es: {promedio:.2f}")
if promedio >= 6 and promedio <= 8:
    print("El rendimiento ha sido aceptable")
elif promedio > 8:
    print("El rendimiento ha sido elevado")
else:
    print("El rendimiento ha sido bajo")

     