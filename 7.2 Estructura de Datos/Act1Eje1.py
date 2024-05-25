personas = []
i=1
while i < 11:
    nombre = input(f"Ingrese el nombre de la persona {i}: ")
    if nombre not in personas:
        personas.append(nombre)
        i += 1
    else:
        print("El nombre ya ha sido ingresado, por favor ingrese un nombre diferente.")
print("Lista de Personas")
print("=================")
for nombre in personas:
    print(nombre)

del personas[2]
del personas[-1]
personas.sort()
print("Lista de Personas")
print("=================")
for nombre in personas:
    print(nombre)
