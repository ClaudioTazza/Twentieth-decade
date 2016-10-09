from personaggio import Personaggio

def eventoIniziale(player):
    Scelta= input("Fai la tua scelta:\n1)Pugnale\n2)Chiave d'oro\n")
    if Scelta== 1:
        player.pwrUp(20)
    if Scelta== 2:
	player.dropGKey()
