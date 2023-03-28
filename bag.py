import random
class Bag:
    def __init__(self) -> None:
        self.points_for_letter = {"A": 1,"B": 3, "C": 3, "D": 2,"E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X":8, "Y": 4, "Z": 10, "BLANK": 0}
        self.letters_in_bag = ["A"]*9 + ["B"]*2 + ["C"]*2 + ["D"]*4 + ["E"]*12 + ["F"]*2 + ["G"]*3 + ["H"]*2 + ["I"]*9 + ["J","K"] + ["L"]*4 + ["M"]*2 + ["N"]*6 + ["O"]*8 + ["P"]*2 + ["Q"] + ["R"]*6 + ["S"]*4 + ["T"]*6 + ["U"]*4 + ["V"]*2 + ["W"]*2 + ["X"]+["Y"]*2 + ["Z"] + ["BLANK"]*2
    
    def draw_letters(self, hand):
        ''' Draw so that you have 7 letters on hand '''
        for _ in range(6):
            letter = random.choice(self.letters_in_bag)
            if len(hand) < 7:
                hand.append(f"{letter}({self.points_for_letter[letter]})")
                self.letters_in_bag.remove(letter)
        return hand


hand = []
l = Bag()
hand = l.draw_letters(hand)
# print(hand)
