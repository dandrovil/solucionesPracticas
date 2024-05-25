"""
Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad. Si el cliente compra más de 12  unidades (y hasta 24 unidades),
el costo tiene un descuento del 10%. Si compra más de 24 unidades, el descuento es del 15%. Además posee la promoción a los jubilados.
La promoción de jubilados es sumarle un 10% de descuento (si posee otros descuentos, se suma los descuentos).
Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.

Analisis:
            Entrada: unidadesDeLeche tipo entero, esJubiado tipo Booleano, descuento tipo flotante
            Proceso: montoParcial tipo flotante
                     montoParcial = unidadesDeLeche * 1000
                     montoTotal = montoParcial * (1-descuento)
                     descuento = descuento * 100
            Salida:  montoTotal tipo flotante
"""
descuento = 0.0
unidadesDeLeche = int(input("Ingrese la cantidad de unidades de leche: "))
esJubiado = int(input("Ingrese 0 si el cliente no es jubilado o 1 si es Jubilado: "))

if  unidadesDeLeche > 12 and unidadesDeLeche <= 24:
    descuento = descuento + 0.10
elif unidadesDeLeche > 24:
    descuento = descuento + 0.15
    
if esJubiado == 1:
    descuento = descuento + 0.10

montoParcial = unidadesDeLeche * 1000
montoTotal = montoParcial * (1-descuento)
descuento = descuento * 100


print(f"El monto sin descuento es: ${montoParcial:.2f}")  
print(f"El descuento es de: {descuento}%")
print(f"El monto con descuento es: ${montoTotal:.2f}")



