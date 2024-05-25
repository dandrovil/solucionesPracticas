personas = {
    "nombre": "",
    "apellido": "",
    "dni": "",
    "email": "",
    "fecha_de_nacimiento": "",
}
familia = {}

for i in range(4):
    print(f"Ingrese los datos de la persona Nº {i+1}")
    personas['nombre'] = input("Ingrese el nombre: ")
    personas['apellido'] = input("Ingrese el apellido: ")
    personas['dni'] = input("Ingrese el DNI: ")
    personas['email'] = input("Ingrese el email: ")
    personas['fecha_de_nacimiento'] = input("Ingrese la fecha de nacimiento: ")
    familia[i] = personas.copy()



print("Diccionario Familia")
print("====================")
for clave, valor in familia.items():
    print(f"{clave}: {valor}")
