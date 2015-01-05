# Always take an action inside a while loop, or it'll go infinite!
# Use while to loop until you have enough hits to kill 10 munchkins.
hits = 0
while hits <10:
    enemy = self.findNearestEnemy()
    if enemy:
        self.attack(enemy)
        hits +=1
self.cleave(enemy)
self.moveXY(79, 33)

# When you're done, retreat to the ambush point.