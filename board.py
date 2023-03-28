from bag import Bag

class Board:
    def __init__(self) -> None:
        self.size = 15
        self.board = [[None] * self.size for _ in range(self.size)]
        self._add_constants()
        self.board_constants = ["DL", "DW", "TL", "TW", "#"]
        self.points_for_letter = Bag().points_for_letter

    def open_dict(self):
        return open("Collins Scrabble Words (2019) with definitions-1.txt", "r")

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

    def place_letters(self, hand, word, start_pos, direction):
        hand = [letter[0] for letter in hand]
        start_col = ord(start_pos[0]) - 65
        start_row = int(start_pos[1]) - 1

        if self.board[7][7] == "#":
            if direction == "H" and (start_row != 7 or start_col + len(word) < 7):
                return "First word of game must be on the '#'"
            if direction == "V" and (start_col != 7 or start_row + len(word) < 7):
                return "First word of game must be on the '#'"
            
        for i in range(len(word)):
            if direction == "H":
                if word[i] not in hand and (self.board[start_row][start_col + i] is None or self.board[start_row][start_col + i] in self.board_constants):
                    return "You do not have the right letters for this word, try again!"
                
                if self.board[start_row][start_col + i] is not None:
                    if self.board[start_row][start_col + i] not in self.board_constants:
                        if self.board[start_row][start_col + i] != f"{word[i]}({self.points_for_letter[word[i]]})":
                            return "Word does not fit in chosen position, try again!"
                        
            elif direction == "V":
                if word[i] not in hand and (self.board[start_row + i][start_col] is None or self.board[start_row + i][start_col] in self.board_constants):
                    return "You do not have the right letters for this word, try again!"
                
                if self.board[start_row + i][start_col] is not None:
                    if self.board[start_row + i][start_col] not in self.board_constants:
                        if self.board[start_row + i][start_col] != f"{word[i]}({self.points_for_letter[word[i]]})":
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
    
# board = Board()
# print(board.place_letters(['Q(2)', 'U(1)', 'E(1)', 'U(1)', 'E(4)', 'Y(4)', 'G(2)'], "QUEUE", "H8", "H"))
# print(board)
# print(board.place_letters(['D(2)', 'O(1)', 'R(1)', 'I(1)', 'H(4)', 'Y(4)', 'G(2)'], "HGRYI", "H8", "V"))
# print(board)
# print(board.place_letters(['D(2)', 'O(1)', 'R(1)', 'E(28)', 'H(4)', 'Y(4)', 'G(2)'], "ORE", "I8", "V"))
# print(board)