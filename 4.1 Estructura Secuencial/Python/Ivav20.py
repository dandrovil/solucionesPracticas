precio = float(input("Ingrese el precio($) del producto: "))
iva = float(input("Ingrese el IVA(%) del producto: "))
impuesto = (iva / 100) + 1
precio_final = precio * impuesto
print(f"El precio final del producto es: ${precio_final:.2f}")