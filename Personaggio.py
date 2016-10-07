class Personaggio:
    def __init__(self,Nickname="unknow",Pwr):
        self.Nickname= Nickname
        self.Pwr= Pwr

    def Choose_Nick(self):
        Nick=raw_input("Salve sfortunato, come vuole essere chiamato?\n")
        self.Nickname= Nick
