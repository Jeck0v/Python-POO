from Perso import Perso
from random import randint

class RoiSorcier(Perso) :
    def __init__(self, name, force, degats):
        super().__init__(name, force, degats)
    
    def frappeAvecSonEpee(self, cible):
        cible.recoitDegat(self.getForce()+5, self.getDegats())

    def attaqueAvecSonNazgul(self,cible):
        cible.recoitDegat(self.getForce()+20, self.getDegats())

    def attaque(self, cible):
        print(self.getNom(), " attaque ", cible.getNom())
        nb = randint(1,3)
        match nb :
            case 1 :
                self.frappeAvecSonEpee(cible)
            case 2 :
                self.attaqueAvecSonNazgul(cible)
            case 3 :
                self.frappe(cible)
    