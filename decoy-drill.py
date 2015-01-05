# We are field testing a new battle unit: the decoy.
# Build 4 decoys, then report the total to Naria.
# Each decoy costs 25 gold. Use the Quartz Sense Stone
# to know when you have more than 25 gold with self.gold.
# Keep a count of decoys you built as you go along.
# Break out of the loop when you have built 4.

while self.gold < 100:
    item = self.findNearestItem()
    if item:
        x = item.pos.x
        y = item.pos.y
        self.moveXY(x, y)
self.buildXY("decoy", 36, 30)
self.buildXY("decoy", 46, 30)
self.buildXY("decoy", 36, 36)    
self.buildXY("decoy", 30, 30)    

self.say("Done building decoys!")
# Go to Naria and say how many decoys you built.
self.moveXY(14, 36)
self.say(4)
