from bag import Bag
from players import Player
from board import Board


def create_players():
    player_list = []
    player_count = int(input("How many players are playing? "))
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

    if opt == "1":
        answer = True
        while answer is not None:
            word = input("Word: ").upper()
            pos = input("Position to place from: ").upper()
            direction = input("Horizontal or Vertical (h/v): ").upper()

            #change pos=c10 to (e.x: 2,3)
            start_col = ord(pos[0]) - 65
            start_row = int(pos[1]) - 1

            #returns score if possible otherwise error
            answer = board.place_letters(player, word, start_col, start_row, direction)

            if answer is not None:
                print(answer)
            if answer == f"{word} is not in dictionary. Turn forfeited":
                answer = None  

        #Refill hand
        bag.draw_letters(player.hand)

        pass_counter = 0
        return pass_counter, word

    elif opt == "2":
        let_swap = input("What letters to swap? (e.x: AFSAS) ").upper()
        bag.swap(player.hand, let_swap)
        pass_counter = 0
        return pass_counter, None

    elif opt == "3":
        pass_counter += 1
        return pass_counter, None

def cal_score(player, word, dict):
    if word is None:
        return
    total_score = 0
    for tile in word:
        for sta in dict:
            if tile == sta:
                total_score += int(dict[sta])

    player.score = total_score

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
        #if all players pass twice (more points wins)
        if pass_counter >= 2*len(player_list):
            print(f"Game Over! (name) has more points!")
            break

        for player in player_list:
            #if player has won
            if bag.letters_in_bag == [] and player.hand == []:
                print(f"Game Over! {player.name} won!")
                return
            
            #draw letters
            bag.draw_letters(player.hand)
            #print board
            print(board)
            pass_counter, word = options(board, bag, player, pass_counter)
            cal_score(player, word, bag.points_for_letter) 
            

            




if __name__ == "__main__":
    main()