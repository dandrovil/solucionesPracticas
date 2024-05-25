Algoritmo Hincha
	// Declaracion de variables
	Definir Ganados, Perdidos, Empatados, Jugados, Puntos Como Entero
	
	// Carga de Datos
	Escribir "Ingrese la cantidad de partidos ganados: "
	Leer Ganados
	Escribir "Ingrese la cantidad de partidos perdidos: "
	Leer Perdidos
	Escribir "Ingrese la cantidad de partidos empatados: "
	Leer Empatados
		
	// Calculo de Datos
	Jugados = Ganados + Perdidos + Empatados
	Puntos = ((Ganados * 3) + Empatados)
	
	// Resultado esperado
	Escribir "El equipo tiene ", Puntos, " puntos de ", Jugados, " partidos jugados."
	
FinAlgoritmo
