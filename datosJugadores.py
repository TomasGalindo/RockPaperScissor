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

def printJugador(myJugador):
    for key in myJugador:
        print(key +  " : " + str(myJugador[key]))   
    print("---------")

#devuelve el diccionario con el jugador
def extraerJugador(myListaJugadores, nombreJugador):
    jugadorDetectado = False
    for element in myListaJugadores:
        indice = myListaJugadores.index(element)
        if nombreJugador == element.get('Nombre'):
            jugadorDetectado = True
            break

    juer = myListaJugadores.pop(indice)
    return juer


#devuelve True or false
def esJugador(myListaJugadores, nombreJugador):
    jugadorDetectado = False
    for element in myListaJugadores:
        if nombreJugador == element.get('Nombre'):
            jugadorDetectado = True
            break
    return jugadorDetectado
    