class cards:

    def __init__(
            self,
            name: str = "unnamed",
            maxHealth : int = 0,
            attack: int = 0
            ):
        self.name = name
        self.maxHealth = maxHealth
        self.health = maxHealth
        self.attack: attack

    def attackCard(self, target):
        target.health -= self.attack