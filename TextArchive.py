from Personaggio import Personaggio

def Story():
    return "'Racconto di una trama affascinante'\n"

def HelloPlayer(player):
    print "Hello, " + player.nickname
    print player.Pwr
    print player.GKeys

#def StatsPlayer(player): Mostra tutte le caratteristiche del personaggio
 

if __name__=='__main__':
    p = Personaggio()
    print helloPlayer(p)
