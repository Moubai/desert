flagGreen = self.findFlag("green")
flagBlack = self.findFlag("black")
flagViolet = self.findFlag("violet")

# If there's a green flag, build a fence.
if flagGreen:
    self.pickUpFlag(flagGreen)
    self.buildXY("fence", self.pos.x+1, self.pos.y)  
# If there's a black flag, build a fire trap
 elif flagBlack:
    self.pickUpFlag(flagBlack)
    self.buildXY("fire-trap", self.pos.x, self.pos.y)      
 # If there's a violet flag, just move to its location.
 elif flagViolet:
    self.pickUpFlag(flagViolet)
# Remember to pick up flags after you're done with them!