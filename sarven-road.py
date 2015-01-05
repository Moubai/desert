# Get to the oasis. Watch out for new enemies: ogre scouts!
# Go up and right by adding to your current X and Y position.
loop:
    # Attack any enemies you see, or keep moving up and right.
    enemy = self.findNearestEnemy()
    
    if enemy and self.distanceTo(enemy) <10:
        self.attack(enemy)
        self.attack(enemy)
    else:
        x = self.pos.x + 10
        y = self.pos.y + 10
        self.moveXY(x, y)