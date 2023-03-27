class Player:
    def __init__(self, name=None, hand=[]) -> None:
        self.name = name
        self.hand = hand
    
    def __str__(self) -> str:
        return self.name