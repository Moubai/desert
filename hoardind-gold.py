# Récolte 25 pièces d'or et indique à Naria le total
# Utilise l'instruction break pour arreter de récolter les pièces quand totalGold >= 25
totalGold = 0
while totalGold <=25:
    coin = self.findNearestItem()
    if coin:
        pos = coin.pos
        x = pos.x
        y = pos.y
        self.moveXY(x, y)
        totalGold = self.gold    
    # Ramasse les pièces et les ajoute à votre total 
    # Permet d'obtenir la valeur :  coin.value
    # Aller voir Naria et dites lui combien d'or vous avez recolé
self.say("Fin de la récolte d'or !")
self.moveXY(58, 33)
self.say(totalGold)
# Aller voir Naria et dites lui combien d'or vous avez recolé