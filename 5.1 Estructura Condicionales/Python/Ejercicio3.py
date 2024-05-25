"""Ingresar el dia de la semana y mostrar un mensaje si se trabaja o se descansa

Analisis:
            Entrada: dia tipo cadena
            Proceso: Condicional evaluar (dia = "sabado" o dia = "domingo")
            Salida: Mensaje tipo cadena
"""

dia = str(input("Que dia es hoy (nombre): "))

if dia.lower() == "sabado" or dia.lower() == "domingo":
    print("Hoy puedes relajarte")
else:
    print("Hoy tienes que trabajar")