# Protect brandy from incoming thirsty yaks!
# Gather gold to build decoys to distract the yaks.
# Use flags to decide when and where to build decoys.
loop:
    coin = self.findNearestItem()
    enemy = self.findNearestEnemy()
    flag = self.findFlag()
    if flag and self.gold >=25:
        self.pickUpFlag(flag)
        x = self.pos.x
        y = self.pos.y
        self.buildXY("decoy", x, y)
    elif coin:
        x = coin.pos.x
        y = coin.pos.y
        self.moveXY(x, y)