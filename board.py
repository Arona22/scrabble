from bag import Bag

class Board:
    def __init__(self) -> None:
        ''' Basics for the board '''
        self.size = 15
        self.board = [[None] * self.size for _ in range(self.size)]
        self.board_constants = ["DL", "DW", "TL", "TW", "#", None]
        self.points_for_letter = Bag().points_for_letter
        self._add_constants()

    def _add_constants(self):
        ''' Add the constants to the board '''
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
        ''' opens the txt file with all the words '''
        return open("Collins Scrabble Words (2019) with definitions-1.txt", "r")
    
    def _check_for_word_vertical(self, row, col, letter_row, letter):
        ''' Returns the word made from the chosen word vertically '''
        word = ""
        while self.board[row][col] not in self.board_constants:
            word += self.board[row][col][0]
            row += 1
            if row == letter_row:
                word += letter
                row += 1
        return word
    
    def _check_for_word_horizontal(self, row, col, letter_col, letter):
        ''' Returns the word made from the chosen word horizontally '''
        word = ""
        while self.board[row][col] not in self.board_constants:
            word += self.board[row][col][0] 
            col += 1
            if col == letter_col:
                word += letter
                col += 1
        return word


    def place_letters(self, player, word, start_col, start_row, direction):
        ''' Check if the words formed are valid and adds them to the board '''
        hand_letters = [letter[0] for letter in player.hand]
        used_letters = []
        made_words = [word]
        letters_scored = []
        connects = False

        # Make sure that the first word is set on the #
        if self.board[7][7] == "#":
            if direction == "H" and (start_row != 7 or start_col + len(word) <= 7):
                return "First word of game must be on the '#'"
            if direction == "V" and (start_col != 7 or start_row + len(word) <= 7):
                return "First word of game must be on the '#'"
            
        for i in range(len(word)):
            letters_scored.append(word[i])

            # Go down if V or to the right if H
            if direction == "H":
                curr_pos = self.board[start_row][start_col + i]
            else:
                curr_pos = self.board[start_row + i][start_col]

            # Add multication
            if curr_pos == "DL":
                letters_scored.append(word[i])
            if curr_pos == "TL":
                for _ in range(2):
                    letters_scored.append(word[i])
            if curr_pos == "DW":
                for letter in word:
                    letters_scored.append(letter)
            if curr_pos == "TW":
                for _ in range(2):
                    for letter in word:
                        letters_scored.append(letter)

            # test for if you chose a letter that should be on hand
            if curr_pos in self.board_constants:
                if word[i] not in hand_letters:
                    return "You do not have the right letters for this word, try again!"
                hand_letters.remove(word[i])
                used_letters.append(word[i])
                
                # check if you made any words on the go
                if direction == "H":
                    new_start = start_row
                    while self.board[new_start - 1][start_col + i] not in self.board_constants:
                        new_start -= 1
                    new_word = self._check_for_word_vertical(new_start, start_col, start_row, word[i])

                if direction == "V":
                    new_start = start_col
                    while self.board[start_row + i][new_start - 1] not in self.board_constants:
                        new_start -= 1
                    new_word = self._check_for_word_horizontal(start_row, new_start, start_col, word[i])
                
                if len(new_word) > 1:
                    made_words.append(new_word)
                    letter_in = True
                    for letter in new_word:
                        if letter == word[i] and letter_in:
                            continue
                    connects = True

            # if you are connecting to a letter
            elif curr_pos != f"{word[i]}({self.points_for_letter[word[i]]})":
                return "Word does not fit in chosen position, try again!"
            
            elif curr_pos == f"{word[i]}({self.points_for_letter[word[i]]})":
                connects = True
        

        if not connects and self.board[7][7] != "#":
            return "word has to be connected to the base, try again!"

        check_words = self._search_dictionary(made_words)
        if check_words is not None:
             print(check_words)
             return
        
        self._add_to_board(word, start_col, start_row, direction)
        for letter in used_letters:
            player.delete_item_in_hand(letter)

        # return the letters that you should get points for
        return letters_scored

    def _search_dictionary(self, made_words):
        ''' Check if all the words formed are in the dictionary '''
        for made_word in made_words:
            invalid_word = True 
            dictionary = self.open_dict()
            for line in dictionary:
                if line.split("\t")[0] == made_word:
                    invalid_word = False
            dictionary.close()

            if invalid_word:
                return f"{made_word} is not in dictionary. Turn forfeited"

    def _add_to_board(self, word, start_col, start_row, direction):
        ''' adds the letters to the board '''
        for i in range(len(word)):
            if direction == "H":
                self.board[start_row][start_col + i] = f"{word[i]}({self.points_for_letter[word[i]]})"
            else:
                self.board[start_row + i][start_col] = f"{word[i]}({self.points_for_letter[word[i]]})"

    def __str__(self) -> str:
        ''' return the board '''
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