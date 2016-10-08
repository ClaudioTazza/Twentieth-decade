#Non so cosa io stia facendo, ma un viaggio di 1000 kilometri inizia sempre con il primo passo

import TextArchive
from personaggio import Personaggio
#import Level
import Events

protagonista = Personaggio()

print TextArchive.story()  #Racconta la trama generale


#Personaggio.Choose_Nick(Protagonista)
protagonista.chooseNick()

Events.eventoIniziale(protagonista)

TextArchive.helloPlayer(protagonista)
