
cotizacion = 1280

pesos = float(input("Ingrese monto en pesos (ARS): "))

dolares = float(pesos / cotizacion)

print(f"{pesos:.0f} Pesos (ARS) a una tasa de cambio de {cotizacion} por dólar equivalen a {dolares:.2f} Dolares (USD)")