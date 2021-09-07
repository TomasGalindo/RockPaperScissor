import os
import archivoJson
import datosJugadores
import RockPaperScissorLogic

def mostrarHistorico(myList):
    if(len(myList) == 0):
        print("VACIO")
    else:
        for element in myList:
            datosJugadores.printJugador(element)

def jugar():
    nombreJugador =input("introduzca nombre: ")
    nombreJugador = RockPaperScissorLogic.tratarNombreUsuario(nombreJugador)
    print("nombreJugador" + nombreJugador)
    jugadorDetectado = datosJugadores.esJugador(myList,nombreJugador)
    if jugadorDetectado:
        myJugador = datosJugadores.extraerJugador(myList,nombreJugador)
        
    else:
        myJugador = datosJugadores.crearJugador(nombreJugador)
    
    ###momento de jugar para actualizar:
    result = RockPaperScissorLogic.play()
    
    myJugador = datosJugadores.modificarJugador(myJugador,result)
    myList.append(myJugador)

"""
Cargamos la base de datos que podremos que la guardamos ne un json
"""
nameFile = archivoJson.NAME_FILE
if(os.path.exists(nameFile)):
    print("existefile")
    myList = archivoJson.lecturaJSON()
else:
    print("No existe File")
    #archivoJson.createFile(nameFile)
    myList = []

#ya tengo mis datos cargados en myList

"""
Cargamos el menu
"""

valor = 0
while(valor != 3):
    print("Menú del juego:")
    print("1-Jugar:")
    print("2-Histórico:")
    print ("3-Salir")
    try:
        valor =int(input("introduzca Valor: "))
        if (valor == 1):
            jugar()
        elif(valor == 2):
            print ("Datos de los jugadores")
            mostrarHistorico(myList)
        elif(valor == 3):
            archivoJson.escrituraJSON(myList)
            print ("saliendo del juego")
        else:
            print ("Seleccione una opcion del 1 al 3")
    except ValueError:
        print("Valor no permitido")
