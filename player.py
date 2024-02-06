
from Weapon import Weapon
class Player:
    def __init__(self,pseudo,health,attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.Weapon = None
        print("Bienvenue", pseudo, "- Health", health, "- Attack", attack)

    def get_Pseudo(self):
            return self.pseudo
    def get_Health(self):
            return self.health
    def get_Attack(self):
            return self.attack
    def damage(self, damage):
        self.health -= damage
        print ('Vous venez de subir', damage , "dégats")

    def attack_player(self, target_player):
        target_player.damage(self.attack)





player1 = Player("Jecko",20,5)
player2 = Player("Algont", 20, 3)

Weapon1 = Weapon("Max", 10)
Weapon2 = Weapon("Noe", 12)

print(player1.attack_player(player2))
print(player1.get_Pseudo(), "attaque et il ne reste que", player2.get_Health(), "point de vie à l'autre joueur")
print(player1.damage(5))
print(player1.get_Health())
print(player1.get_Pseudo(),"à ajouter une arme, il peut désomais faire", player1.get_Attack() + Weapon1.degatsWeapon(), "dégats, par attaque")
print(player1.Weapon1)
