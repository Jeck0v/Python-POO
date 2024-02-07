class Perso :
    def __init__(self, name, force, degats):
        self.__name = name
        self.__vie = 100
        self.__force = force
        self.__exp = 0
        self.__degats = degats



    #getter / setter

    def getNom(self):
        return self.__name

    def setNom(self,name):
        self.__name = name

    def getForce(self):
        return self.__force

    def setForce(self,force):
        self.__force=force

    def getDegats(self):
        return self.__degats

    def setDegats(self,degats):
        self.__degats=degats

    def getExp(self):
        return self.__exp

    def setExperience(self, exp):
        self.__exp=exp

    def getVie(self):
        return self.__vie

    def setVie(self,vie):
        self.__vie=vie



    def frappe(self,cible):
        if cible.esquive == False:
            self.recoitDegat(cible, (self.__force+self.__exp), self.__degats)
        else:
            print('frappe esquivé')




    def esquive(self):
        if randint(1,4) == 1:
            return True
        else:
            return False

    def recoitDegat(self, force, degats):
        degats_recu = force + degats
        print(self.getNom(), " a recu", degats_recu, "degats !")
        self.__vie -= degats_recu
        print("Il lui reste", self.__vie, " points de vie")

