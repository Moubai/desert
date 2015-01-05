loop:
    currentHealth = self.health
    healingThreshold = self.maxHealth / 2
    enemy = self.findNearestEnemy()
    # If your current health is less than the threshold,
    # move to the healing point and say, "heal me".
    # Otherwise, attack. You'll need to fight hard!
    if currentHealth < healingThreshold:
        self.moveXY(65, 46)
        self.say("heal me")
    elif enemy:
        if self.isReady("cleave"):
            self.cleave()
        else:
            self.attack(enemy)
            self.attack(enemy)