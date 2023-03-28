from bag import Bag

class Board:
    def __init__(self) -> None:
        self.size = 15
        self.board = [[None] * self.size for _ in range(self.size)]
        self.board_constants = ["DL", "DW", "TL", "TW", "#"]
        self.points_for_letter = Bag().points_for_letter
        self._add_constants()

    def _add_constants(self):
        for row in range(self.size):
            for col in range(self.size):
                if row == col or row + col == self.size - 1:
                    if row == 5 or row == 9:
                        self.board[row][col] = "TL"
                    elif row == 6 or row == 8:
                        self.board[row][col] = "DL"
                    else:
                        self.board[row][col] = "DW"

                if row % 7 == 0 and col % 7 == 0:
                    if col == 0:
                        self.board[row][col + 3] = "DL"
                    elif col == 14:
                        self.board[row][col - 3] = "DL"
                    self.board[row][col] = "TW"

        self.board[1][5] = "TL"
        self.board[1][9] = "TL"
        self.board[5][1] = "TL"
        self.board[5][13] = "TL"
        self.board[9][13] = "TL"
        self.board[9][1] = "TL"
        self.board[13][5] = "TL"
        self.board[13][9] = "TL"
        self.board[2][6] = "DL"
        self.board[2][8] = "DL"
        self.board[3][0] = "DL"
        self.board[3][7] = "DL"
        self.board[3][14] = "DL"
        self.board[6][2] = "DL"
        self.board[6][12] = "DL"
        self.board[7][3] = "DL"
        self.board[7][11] = "DL"
        self.board[8][2] = "DL"
        self.board[8][12] = "DL"
        self.board[11][0] = "DL"
        self.board[11][7] = "DL"
        self.board[11][14] = "DL"
        self.board[12][6] = "DL"
        self.board[12][8] = "DL"
        self.board[7][7] = "#"

    def open_dict(self):
        return open("Collins Scrabble Words (2019) with definitions-1.txt", "r")

    def place_letters(self, player, word, start_col, start_row, direction):
        hand_letters = [letter[0] for letter in player.hand]
        used_letters = []

        if self.board[7][7] == "#":
            if direction == "H" and (start_row != 7 or start_col + len(word) <= 7):
                return "First word of game must be on the '#'"
            if direction == "V" and (start_col != 7 or start_row + len(word) <= 7):
                return "First word of game must be on the '#'"
            
        for i in range(len(word)):
            if direction == "H":
                curr_pos = self.board[start_row][start_col + i]
            elif direction == "V":
                curr_pos = self.board[start_row + i][start_col]

            if curr_pos is None or curr_pos in self.board_constants:
                if word[i] not in hand_letters:
                    return "You do not have the right letters for this word, try again!"
                else:
                    used_letters.append(word[i])
            
            if curr_pos is not None and curr_pos not in self.board_constants and curr_pos != f"{word[i]}({self.points_for_letter[word[i]]})":
                return "Word does not fit in chosen position, try again!"
        
        invalid_word = True 
        dictionary = self.open_dict()
        for line in dictionary:
            if line.split("\t")[0] == word:
                invalid_word = False
        dictionary.close()
        
        if invalid_word:
            return f"{word} is not in dictionary. Turn forfeited"
        
        for i in range(len(word)):
            if direction == "H":
                self.board[start_row][start_col + i] = f"{word[i]}({self.points_for_letter[word[i]]})"
            else:
                self.board[start_row + i][start_col] = f"{word[i]}({self.points_for_letter[word[i]]})"

        for letter in used_letters:
            player.delete_item_in_hand(letter)

    def calculate_score(self, letter_pos, direction):
        pass

    def __str__(self) -> str:
        counter = 1
        return_string = "       A      B      C      D      E      F      G      H      I      J      K      L      M      N      O\n"
        return_string += "    " + "=" * 105 + "\n"
        for row in self.board:
            return_string += "{:3}|".format(counter)
            for col in row:
                if col is None:
                    return_string += "      |"
                else:
                    return_string += f"{col.center(6)}|"
            return_string += "\n" + "    " + "-" * 105 + "\n"
            counter += 1
        return return_string