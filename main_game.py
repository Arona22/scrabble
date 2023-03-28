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

def options(board, bag, player):
    print(f"{player.name}'s turn!")
    print("1. Play a word")
    print("2. Swap letters")
    print("3. Pass your turn")
    player.print_hand()
    opt = input("CHOOSE MOVE: ")
    if opt == "1":
        pos = input("Position: ").upper()
        direction = input("Horizontal or Vertical (h/v): ").upper()
        word = input("Word: ").upper()
        board.place_letters(player.hand, word, pos, direction)

    elif opt == "2":
        let_swap = input("What letters to swap? (e.x: AFSAS) ").upper()
        bag.swap(player.hand, let_swap)

    elif opt == "3":
        return


def main():
    #make players
    player_list = create_players()
    #make bag
    bag = Bag()
    #make board
    board = Board()

    end = True
    while end == True:
        for player in player_list:
            #draw letters
            bag.draw_letters(player.hand)
            #print board
            print(board)
            options(board, bag, player)
            











if __name__ == "__main__":
    main()