class Personaggio:
    def __init__(self, nickname="unknown", Pwr=0):
        self.nickname= nickname
        self.Pwr= Pwr
	self.GKeys= 0

    def chooseNick(self):
        nick = raw_input("Salve sfortunato, come vuole essere chiamato?\n> ")
        self.nickname = nick

    def DropGKey(self):
	self.GKeys+= 1

    def PwrUp(self,num):
	self.Pwr+= num

if __name__=='__main__':
    p = Personaggio()
    print "Creato il Personaggio p"
    print "p nickname:", p.nickname
    print "p pwr:", p.pwr

    print "p chooseNick"
    p.chooseNick()

    print "p nickname now is:", p.nickname
