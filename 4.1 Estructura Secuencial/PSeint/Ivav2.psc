Algoritmo IVAv2
	// Declaracion de variables
	Definir Precio, Iva, Impuesto, PrecioFinal Como Real
	
	// Carga de Datos
	Escribir "Ingrese el precio($) del producto: "
	Leer Precio
	Escribir "Ingrese el IVA(%) del producto: "
	Leer Iva
	
	// Calculo de Datos
	Impuesto = (Iva / 100) + 1
	PrecioFinal = Precio * Impuesto
	
	// Resultado esperado
	Escribir "El precio final del producto es: $", PrecioFinal
	
FinAlgoritmo
