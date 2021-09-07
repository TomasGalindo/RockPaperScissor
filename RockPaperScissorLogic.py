"""
juego de piedra papel y tijera
"""
import random
def tratarEleccion(palabra):
    solucion = palabra.strip().lower()
    return solucion

def tratarNombreUsuario(palabra):
    solucion = palabra.strip().capitalize()
    return solucion

def game_logic(pc_chose,player_chose):
    result=""
    whoWins=""
    if (pc_chose == "rock"):
        if player_chose == "rock":
            result = "E"
            whoWins = "DRAW"
        elif player_chose == "paper":
            result = "V"
            whoWins = "Player_Wins"
        elif player_chose == "scissor":
            result = "D"
            whoWins = "PC wins"
    elif(pc_chose == "paper"):
        if player_chose == "rock":
            result = "C"
            whoWins = "PC wins"
        elif player_chose == "paper":
            result = "E"
            whoWins = "DRAW"
        elif player_chose == "scissor":
            result = "V"
            whoWins = "Player wins"
    elif(pc_chose == "scissor"): # pc chose = scissors
        if player_chose == "rock":
            result = "V"
            whoWins = "Player wins"
        elif player_chose == "paper":
            result = "D"
            whoWins = "PC wins"
        elif player_chose == "scissor":
            result = "E"
            whoWins = "DRaW"

    print(whoWins)
    return result


def play():
    elements = ["rock","paper","scissor"]    
    pcChose = random.choice(elements)
    playerChose = ""
    while (not playerChose in elements):
        playerChose = input("Elige(rock,paper,scissor): ")
        playerChose = tratarEleccion(playerChose)

    print("Pc Chose = " + pcChose)
    print("Player Chose = " + playerChose)

    result = game_logic(pcChose,playerChose)
    return result
    
