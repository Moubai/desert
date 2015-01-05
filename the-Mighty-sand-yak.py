# Laissez les yaks approcher, puis déplacez vous 10m à droite pour esquiver.
# Esquivez 4 yaks pour compléter le niveau.

loop:
    # Utilisez "if" pour vous déplacer uniquement lorsqu'un yak est à 10m.
    enemy = self.findNearestEnemy()
    dist = self.distanceTo(enemy)
    location = self.pos

    if dist < 10:
        if location = 80,30:
            x = self.pos.x +5
            y = self.pos.y
            self.moveXY(x, y)
        elif location > 6,30:
            x = self.pos.x + 5
            y = self.pos.y
            self.moveXY(x, y)