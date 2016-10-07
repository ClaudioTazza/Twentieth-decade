from Personaggio import Personaggio

def story():
    return "'Racconto di una trama affascinante'\n"

def helloPlayer(player):
    return "Hello, " + player.nickname


if __name__=='__main__':
    p = Personaggio()
    print helloPlayer(p)
