"""Ingresar un nombre de usuario y una contraeña si ambos son la palabra "admin" conceder acceso caso contrario no.

Analisis:
            Entrada: user, password tipo cadena
            Proceso: Condicional evaluar (user = "admin" y password = "admin")
            Salida:  Mensaje tipo cadena
"""

user = str(input("Ingrese nombre de usuario: "))
password = str(input("Ingrese contraseña: "))

if user == "admin" and password == "admin":
    print("Acceso concedido")
else:
    print("Acceso denegado")
    
