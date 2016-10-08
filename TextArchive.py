from personaggio import Personaggio

def Story():
    return "'Racconto di una trama affascinante'\n"

def helloPlayer(player):
    print "Hello, " + player.nickname
    print player.Pwr
    print player.GKeys

def StatsPlayer(player):
    print "#######################\n"\
          "    ", player.nickname,\
          "\nPwr: ", player.Pwr,\
          "\nChiavi d'oro: ", player.GKeys,\
          "\n#######################"


if __name__=='__main__':
    p = Personaggio()
    p.chooseNick()
    StatsPlayer(p)
