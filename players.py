class Player:
    def __init__(self, name=None) -> None:
        self.name = name
        self.hand = []

    def print_hand(self):
        print(f"Hand: {str(self.hand)}")
    