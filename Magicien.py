from Perso import Perso
from random import randint

class Magicien(Perso) :
    def lanceUnSort(self, cible):
        nb = randint(1,2) #mettre le nombre de sorts total dans la 2eme valeur
        match nb :
            case 1 :
                self.LanceUnRayonDeLumièreSombre(cible)
            case 2 :
                self.LanceUnRayonDeFeuNoir(cible)

        #rajouter d'autres case quand il y a + de sort



    def LanceUnRayonDeLumièreSombre(self, cible):
        cible.recoitDegat(self.getForce()+10, self.getDegats())
        
    def LanceUnRayonDeFeuNoir(self, cible):
        cible.recoitDegat(self.getForce()+15, self.getDegats())

    def attaque(self, cible):
        print(self.getNom(), " attaque ", cible.getNom())
        match randint(1,2):
            case 1:
                self.lanceUnSort(cible)
            case 2:
                self.frappe(cible)
            