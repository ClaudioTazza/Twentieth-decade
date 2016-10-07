class Personaggio:
    def __init__(self, nickname="unknown", pwr=0):
        self.nickname = nickname
        self.pwr = pwr

    def chooseNick(self):
        nick = raw_input("Salve sfortunato, come vuole essere chiamato?\n> ")
        self.nickname = nick


if __name__=='__main__':
    p = Personaggio()
    print "Creato il Personaggio p"
    print "p nickname:", p.nickname
    print "p pwr:", p.pwr

    print "p chooseNick"
    p.chooseNick()

    print "p nickname now is:", p.nickname
