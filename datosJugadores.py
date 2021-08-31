"""
en este archivo se encuentran todas las operaciones referidas a los jugadores y a la modificación
de sus datos
"""
import archivoJson
#hallar porcentaje
def porcentajeVictorias(victorias,p_jugadas):
    return victorias/p_jugadas

def crearJugador(nombre):
    myJugador = {
        "Nombre":nombre,
        "Victorias":0,
        "Derrotas": 0,
        "Empates":0,
        "PartidasJugadas":0,
        "Victorias%":0
    }

    return myJugador

def modificarJugador(jugador,finJuego): #jugador va a ser el jugador entero (el diccionario)
    
    jugador['PartidasJugadas'] = jugador['PartidasJugadas']+1
    #si finJuego = "V" --> victoria
    #si finJuego = "D" --> derrota
    #si fin juego = "E" --> empate
    if(finJuego == "V"):
        jugador['Victorias'] = jugador['Victorias']+1
    elif(finJuego == "D"):
        jugador['Derrotas'] = jugador['Derrotas']+1
    elif(finJuego == "E"):
        jugador['Empates'] = jugador['Empates']+1
        
    jugador['Victorias%'] = porcentajeVictorias(jugador['Victorias'],jugador['PartidasJugadas'])
    
    return jugador
    print("HOLA")

def printJugador(myJugador):
    for key in myJugador:
        print(key +  " : " + str(myJugador[key]))


"""
tendre un diccionario con los datos del jugador

y si ha ganado o perdido

"""

prueba = crearJugador("Juan")

printJugador(prueba)
print("------------------------------")
prueba = modificarJugador(prueba,"V")
prueba = modificarJugador(prueba,"D")
prueba = modificarJugador(prueba,"D")
prueba = modificarJugador(prueba,"D")
prueba = modificarJugador(prueba,"D")
prueba = modificarJugador(prueba,"E")
prueba = modificarJugador(prueba,"E")
prueba = modificarJugador(prueba,"V")
prueba = modificarJugador(prueba,"V")

prueba2 = crearJugador("Maria")
printJugador(prueba2)
prueba2 = modificarJugador(prueba2,"V")
prueba2 = modificarJugador(prueba2,"V")
prueba2 = modificarJugador(prueba2,"V")
prueba2 = modificarJugador(prueba2,"V")
prueba2 = modificarJugador(prueba2,"E")
prueba2 = modificarJugador(prueba2,"E")
prueba2 = modificarJugador(prueba2,"E")
prueba2 = modificarJugador(prueba2,"V")
prueba2 = modificarJugador(prueba2,"V")






printJugador(prueba)
print("-------------")
printJugador(prueba2)

myListJugadores = []
myListJugadores.append(prueba)
myListJugadores.append(prueba2)

archivoJson.escrituraJSON(myListJugadores)