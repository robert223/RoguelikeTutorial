class cards:

    def __init__(
            self,
            name: str = "unnamed",
            symbol: str = "?",
            health: int = 0,
            attack: int = 0,
            ):
        self.name = name
        self.symbol = symbol
        self.health = health
        self.attack: attack