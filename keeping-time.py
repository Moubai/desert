# Use your new skill to choose what to do: self.now()

loop:
    # If it's the first 10 seconds, fight.
    enemy = self.findNearestEnemy()
    if self.now() < 10:
        if enemy:
            dist = self.distanceTo(enemy)
            if self.isReady("cleave") and dist < 3:
                self.cleave(enemy)
            else:
                self.attack(enemy)
    elif self.now() < 30:
        
        item = self.findNearestItem()
        if item:
            pos = item.pos
            x = pos.x
            y = pos.y
            self.moveXY(x, y)
        
    # Else, if it's the first 30 seconds, collect coins.
    # After 30 seconds, join the raid!
