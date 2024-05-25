personas = {
    "nombre": "",
    "apellido": "",
    "dni": "",
    "email": "",
    "fecha_de_nacimiento": "",
}

personas['nombre'] = input("Ingrese el nombre: ")
personas['apellido'] = input("Ingrese el apellido: ")
personas['dni'] = input("Ingrese el DNI: ")
personas['email'] = input("Ingrese el email: ")
personas['fecha_de_nacimiento'] = input("Ingrese la fecha de nacimiento: ")

print("Diccionario Personas")
print("====================")
for clave, valor in personas.items():
    print(f"{clave}: {valor}")
