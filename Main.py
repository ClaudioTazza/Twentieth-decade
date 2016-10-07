#Non so cosa io stia facendo, ma un viaggio di 1000 kilometri inizia sempre con il primo passo

import TextArchive
from Personaggio import Personaggio
#import Level
#import Events

protagonista = Personaggio()

print TextArchive.story()  #Racconta la trama generale


#Personaggio.Choose_Nick(Protagonista)
protagonista.chooseNick()

print TextArchive.helloPlayer(protagonista)

#Events.EventoIniziale()
