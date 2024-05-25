"""Un hincha de fútbol desea conocer la cantidad de puntos que su equipo lleva acumulados en el campeonato, para ello recibe cada semana la
información de la cantidad total de partidos, desde el inicio del campeonato, que el equipo ha perdido, ha empatado y ha ganado. Por cada
partido empatado recibe un punto, por cada partido ganado tres puntos y por los perdidos cero puntos.

Analisis:
            Entrada: ganados, perdidos, empatados tipo entero
            Proceso: jugados tipo entero
                     jugados = ganados + perdidos + empatados
                     puntos = (ganados * 3) + empatados
             Salida: puntos tipo entero       
"""

ganados = int(input("Ingrese la cantidad de partidos ganados: "))
perdidos = int(input("Ingrese la cantidad de partidos perdidos: "))
empatados = int(input("Ingrese la cantidad de partidos empatados: "))
jugados = ganados + perdidos + empatados
puntos = (ganados * 3) + empatados
print(f"El equipo tiene {puntos} puntos de {jugados} partidos jugados.")