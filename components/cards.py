class Cards:
    
    def __init__(
            self,
            name: str = "unnamed",
            max_health : int = 0,
            attack: int = 0
            ):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.attack: attack

    def card_attack(self, target):
        target.health -= self.attack