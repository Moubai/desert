# Avancez pour atteindre l'oasis
# mais reculez pour éviter les Yaks a proximité
loop:
    enemy = self.findNearestEnemy()
    if enemy and self.distanceTo(enemy) < 10:
        # Déplacez-vous à gauche en soustrayant 10 de vos coordonnées X
        pass
        x = self.pos.x -7
        y = self.pos.y
        self.moveXY(x, y)
    else:
        # Déplacez-vous à droite en additionnant 10 à vos coordonnées X
        pass
        x = self.pos.x +10
        y = self.pos.y
        self.moveXY(x, y)