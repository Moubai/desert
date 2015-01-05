# Get to the oasis,
# fencing off paths with yaks on them as you go.
loop:
    yak = self.findNearestEnemy()
    if yak:
        # If the yak is above you, build a fence 10m below it.
        if yak.pos.y < 30:
            x = self.pos.x
            y = self.pos.y -5
            self.buildXY("fence", x, y)
        elif yak.pos.y >30 :
            # If the yak is below you, build a fence 10m above it.
            x = self.pos.x
            y = self.pos.y +5
            self.buildXY("fence", x, y)
        pass
    else:
        # Move right 10m towards the oasis.
        x = self.pos.x +10
        y = self.pos.y
        self.moveXY(x, y)