class Player:
    def __init__(self, name=None) -> None:
        self.name = name
        self.hand = []
        self.score = 0

    def print_hand(self):
        print(f"Hand: {str(self.hand)}")

    def print_score(self):
        print(f"Score: {self.score}")
        
    def find_item_in_hand(self, letter):
        for i in letter:
            for j in self.hand:
                if j[0] == i:
                    return j

    def delete_item_in_hand(self, letter):
        letter = self.find_item_in_hand(letter)
        self.hand.remove(letter)

    