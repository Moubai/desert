# while-loops repeat until the condition is false.
# Always take an action inside a while loop, or it'll go infinite!
ordersGiven = 0
while ordersGiven < 5:
    # Move and order each of your allies into battle.
    self.say("Attack!")
    x = self.pos.x
    y = self.pos.y-10
    self.moveXY(x, y)
    ordersGiven = ordersGiven+1
    self.say("Attack!")
self.moveXY(56, 31)
loop:
    enemy = self.findNearestEnemy()
    if enemy and self.distanceTo(enemy) < 5:
        if self.isReady("cleave"):
            self.cleave(enemy)
        else:
            self.attack(enemy)