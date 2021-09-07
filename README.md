# RockPaperScissor
Juego de Piedra Papel Tijeras

Para este juego el jugador se enfrentará a la máquina.

El PC elige de forma aleatoria una opcion (piedra, papel tijeras)
y el jugador introduce su opción. El programa decide quien gana.

Se ha llevado a cabo una base de datos simple guardando los elementos en un archivo 
JSON.
Cada usuario esta representado por un diccionario con los siguientes elementos:
     -Nombre
     -Victorias
     -Derrotas
     -Empates
     -%Victorias
	
Si existieran más jugadores, se guardan en una lista.

Para este ejemplo no se va a distinguir las mayúsculas, es decir, 
Juan == juan == JUAN. 
Lo mismo ocurre para los elementos del juego ROCK == rOCK == rock

