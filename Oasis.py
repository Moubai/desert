# Avancez pour atteindre l'oasis
# mais reculez pour �viter les Yaks a proximit�
loop:
    enemy = self.findNearestEnemy()
    if enemy and self.distanceTo(enemy) < 10:
        # D�placez-vous � gauche en soustrayant 10 de vos coordonn�es X
        pass
        x = self.pos.x -7
        y = self.pos.y
        self.moveXY(x, y)
    else:
        # D�placez-vous � droite en additionnant 10 � vos coordonn�es X
        pass
        x = self.pos.x +10
        y = self.pos.y
        self.moveXY(x, y)