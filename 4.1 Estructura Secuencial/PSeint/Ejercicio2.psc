Algoritmo Pintor
	// Declaracion de variables
	Definir Alto, Ancho, Superficie, Manodeobra Como Real
	
	// Carga de Datos
	Escribir "Ingrese el alto de la pared: "
	Leer Alto
	Escribir "Ingrese el ancho de la pared: "
	Leer Ancho
	Escribir "Ingrese el costo por metro cuadrado: "
	Leer Costo
		
	// Calculo de Datos
	Superficie = Alto * Ancho
	Manodeobra = Superficie * Costo
	
	// Resultado esperado
	Escribir "La mano de obra para pintar una pared de ", Alto " por ", Ancho " metros es: $", Manodeobra
	
FinAlgoritmo
