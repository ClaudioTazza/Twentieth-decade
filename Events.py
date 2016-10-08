from Personaggio import Personaggio

def EventoIniziale(player):
    Scelta= input("Fai la tua scelta:\n1)Pugnale\n2)Chiave d'oro\n")
    if Scelta== 1:
        player.PwrUp(20)
    if Scelta== 2:
	player.DropGKey()
 
