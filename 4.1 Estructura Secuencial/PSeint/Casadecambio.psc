Algoritmo Casadecambio
	// Declaracion de variables
	Definir Pesos, Cotizacion, Dolares Como Real
	Cotizacion = 1280
	// Carga de Datos
	Escribir "Ingrese monto en pesos(ARS): "
	Leer Pesos
			
	// Calculo de Datos
	Dolares = Pesos / Cotizacion
		
	// Resultado esperado
	Escribir Pesos, " Pesos(ARS) a una tasa de cambio de ", Cotizacion " por dolar equivalen a ", Dolares, " Dolares(USD)"
	
FinAlgoritmo
