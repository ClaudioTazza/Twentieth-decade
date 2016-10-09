from personaggio import Personaggio

def Story():
    return "'Racconto di una trama affascinante'\n"

def helloPlayer(player):
    print "Hello, " + player.nickname
    print player.pwr
    print player.gKeys

def StatsPlayer(player):
    print "#######################\n"\
          "    ", player.nickname,\
          "\nPwr: ", player.pwr,\
          "\nChiavi d'oro: ", player.gKeys,\
          "\n#######################"


if __name__=='__main__':
    p = Personaggio()
    p.chooseNick()
    StatsPlayer(p)
