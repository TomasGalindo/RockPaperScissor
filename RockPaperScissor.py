"""
juego de piedra papel y tijera
"""
import random

def game_logic(pc_chose,player_chose):
    whoWins=""
    if (pc_chose == "rock"):
        if player_chose == "rock":
            whoWins = "DRAW"
        elif player_chose == "paper":
            whoWins = "Player_Wins"
        elif player_chose == "scissor":
            whoWins = "PC wins"
    elif(pc_chose == "paper"):
        if player_chose == "rock":
            whoWins = "PC wins"
        elif player_chose == "paper":
            whoWins = "DRAW"
        elif player_chose == "scissor":
            whoWins = "Player wins"
    elif(pc_chose == "scissor"): # pc chose = scissors
        if player_chose == "rock":
            whoWins = "Player wins"
        elif player_chose == "paper":
            whoWins = "PC wins"
        elif player_chose == "scissor":
            whoWins = "DRaW"

    print(whoWins)



elements = ["rock","paper","scissor"]
pcChose = random.choice(elements)

playerChose = ""
while (not playerChose in elements):
    playerChose = input("Elige(rock,paper,scissor)")


print("Pc Chose = " + pcChose)
print("Player Chose = " + playerChose)

game_logic(pcChose,playerChose)

"""
Mi intencion para este programa es que se lea de un archivo inicial y que se guarde datos
o que los lea posteriormente
(tener una base de datos)
Nombre Jugador
Victorias
derrotas
Partidas Jugadas
%victorias

tendre un data = [] para que me guarde los jugadores
Jugador sera un diccionario
    

Voy a tener un menu:
Jugar
    pedira el nombre
    se juega
    Se meten los datos en el archivo
Historico
    se lee el archivo
    se muestra como una tabla (como se quiera)



"""