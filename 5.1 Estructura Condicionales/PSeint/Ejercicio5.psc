Algoritmo Ejercicio5
	
	Definir descuento Como Real
	Definir unidadesDeLeche Como Entero
	Definir esJubilado Como Logico
	
	descuento = 0
	
	Escribir "Ingrese la cantidad de unidades de leche: " 
	Leer unidadesDeLeche
	Escribir "Ingrese 0 si el cliente no es jubilado o 1 si es Jubilado: "
	Leer esJubilado
	
	Si unidadesDeLeche > 12 y unidadesDeLeche <= 24 Entonces
		descuento = descuento + 0.10
	SiNo
		Si unidadesDeLeche > 24 Entonces
			descuento= descuento + 0.15
		Fin Si
	Fin Si
	Si esJubilado == Verdadero Entonces
		descuento = descuento + 0.10
	Fin Si
	
	montoParcial = unidadesDeLeche * 1000
	montoTotal = montoParcial * (1-descuento)
	descuento = descuento * 100
	
	Escribir "El monto sin descuento es: $", montoParcial
	Escribir "El descuento es: ", descuento,"%"
	Escribir "El monto con descuento es: $", montoTotal
	
FinAlgoritmo
