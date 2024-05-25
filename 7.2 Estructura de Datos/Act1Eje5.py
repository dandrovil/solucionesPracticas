numeros = []

n = int(input("Ingrese un numero: "))

for i in range(n):
    if i % 2 == 0:
        numeros.append(i)
pares = tuple(numeros)
print("Los primeros", len(pares), "números pares son:")
for i in pares:
    print(i)    
    