from bag import Bag
from players import Player
from board import Board


def create_players():
    while True:
        player_list = []
        player_count = int(input("How many players are playing? "))

        if player_count < 2 or player_count > 4:
            print("Players have to be 2-4")
            continue

        for i in range(player_count):
            #make player
            player = Player()
            input_name = input(f"Name of player {i+1}: ")
            player.name = input_name
            player_list.append(player)
        return player_list        

def options(board, bag, player, pass_counter):

    print(f"{player.name}'s turn!")
    player.print_score()
    print("1. Play a word")
    print("2. Swap letters")
    print("3. Pass your turn")
    player.print_hand()
    opt = input("CHOOSE MOVE: ")
            
    #play word option
    if opt == "1":
        answer = ""
        while type(answer) != list:
            word = input("Word: ").upper()
            pos = input("Position to place word (e.x: h8): ").upper()
            direction = input("Horizontal or Vertical (h/v): ").upper()

            #change pos=c10 to (e.x: 2,3)
            start_col = ord(pos[0]) - 65
            start_row = int(pos[1:]) - 1

            #returns score if possible otherwise error
            answer = board.place_letters(player, word, start_col, start_row, direction)

            #calculate score if answer was valid
            if type(answer) == list:
                if len(word) >= 7:
                    player.score += 50
                    
                cal_score(player, answer, bag.points_for_letter)

            if answer is None:
                break
            if type(answer) == str:
                print(answer)

        #Refill hand
        bag.draw_letters(player.hand)

        pass_counter = 0
        return pass_counter

    #swap option
    elif opt == "2":
        let_swap = input("What letters to swap? (e.x: AFSAS) ").upper()
        bag.swap(player.hand, let_swap)
        pass_counter = 0
        return pass_counter

    #pass option
    elif opt == "3":
        pass_counter += 1
        return pass_counter

def cal_score(player, letters, bag):
    ''' Calculate the score of a round '''
    if letters is None:
        return
    total_score = 0
    for letter in letters:
        for let in bag:
            if letter == let:
                total_score += int(bag[let])

    player.score += total_score

def main():
    ''' Main game loop '''
    #make players
    player_list = create_players()
    #make bag
    bag = Bag()
    #make board
    board = Board()

    #how many titurn players have passed
    pass_counter = 0
    while True:

        for player in player_list:
            #if all players pass twice (more points wins)
            if pass_counter >= 2*len(player_list):
                highscore = 0
                highscorename = ""
                #check who has highscore
                for p in player_list:
                    if p.score > highscore:
                        highscore = p.score
                        highscorename = p.name
                print()
                print()
                print(f"Game Over!")
                if highscorename == "":
                    print("No one won! All players had 0 points")
                    return
                print(f"{highscorename} won with {highscore} points!")
                return
            
            #if player has won
            if bag.letters_in_bag == [] and player.hand == []:
                print()
                print()
                print(f"Game Over! {player.name} won! Score: {player.score}")
                return
            
            #draw letters
            bag.draw_letters(player.hand)
            #print board
            print(board)
            pass_counter = options(board, bag, player, pass_counter)
            

            




if __name__ == "__main__":
    main()