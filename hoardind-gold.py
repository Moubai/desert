# R�colte 25 pi�ces d'or et indique � Naria le total
# Utilise l'instruction break pour arreter de r�colter les pi�ces quand totalGold >= 25
totalGold = 0
while totalGold <=25:
    coin = self.findNearestItem()
    if coin:
        pos = coin.pos
        x = pos.x
        y = pos.y
        self.moveXY(x, y)
        totalGold = self.gold    
    # Ramasse les pi�ces et les ajoute � votre total 
    # Permet d'obtenir la valeur :  coin.value
    # Aller voir Naria et dites lui combien d'or vous avez recol�
self.say("Fin de la r�colte d'or !")
self.moveXY(58, 33)
self.say(totalGold)
# Aller voir Naria et dites lui combien d'or vous avez recol�