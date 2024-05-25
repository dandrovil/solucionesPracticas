Algoritmo Ejercicio_3
	
    Definir Nombre Como Cadena
	Definir Estado Como Logico
	Estado = Verdadero
	
    Mientras Estado Hacer
        Escribir "Ingrese un nombre (fin para terminar): "
        Leer Nombre
        
		Si nombre <> "fin" Entonces
			Escribir "El nombre ingresado es: ", Nombre
		SiNo
			Estado = Falso
        FinSi
        
    FinMientras
	
FinAlgoritmo
