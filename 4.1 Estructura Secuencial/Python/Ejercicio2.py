"""Un pintor de casas debe hacer un presupuesto para un cliente. Lo que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El cliente 
le indica que necesita conocer el costo de mano de obra para pintar una pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro
cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para pintar la pared.

Analisis:
            Entrada: alto, ancho, costo tipo flotante
            Proceso: superficie tipo flotante
                     superficie = alto * ancho
                     manodeobra = superficie * costo
            Salida:  manodeobra tipo flotante
"""


alto = float(input("Ingrese el alto de la pared: "))
ancho = float(input("Ingrese el ancho de la pared: "))
costo = float(input("Ingrese el costo por metro cuadrado: "))
superficie = alto * ancho
manodeobra = superficie * costo
print(f"La mano de obra para pintar una pared de {alto} por {ancho} metros es: ${manodeobra:.2f}")