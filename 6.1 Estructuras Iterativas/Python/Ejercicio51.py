"""Un profesor de matemática necesita generar la tabla de multiplicar de un número entero comprendido entre 1 y 10. Por ejemplo para el 3 debería aparecer como salida:
3x1=3
3x2=6
3x3=9
…. y así hasta 10
"""

tabla = int(input("Que tabla de multiplicar desea visualizar: "))
print(f"Tabla del {tabla}")
print("============")
for i in range(10):
    print(f"{tabla} x {i+1} = {tabla * (i+1)}")
    
    