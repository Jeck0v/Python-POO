from random import shuffle
from Magicien import Magicien
from RoiSorcier import RoiSorcier

class Combat:
    def __init__(self):
        nb_de_tours = 0

    def demarrerCombat(self, Magicien, RoiSorcier):
        def verif_vie(Perso):
            if Perso.getVie() <= 0 : 
                print(Perso.getNom()," est mort")
                return True
            
        order = [Magicien,RoiSorcier]
        shuffle(order)

        while True :
            order[0].attaque(order[1])
            if verif_vie(order[1]): break
            order.reverse()
            print("\r\n")


test = Combat()
test.demarrerCombat(Magicien("Arnaud",10,10),RoiSorcier("Louis",10,10))


