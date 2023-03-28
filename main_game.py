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

def options(board, bag):
    print("CHOOSE MOVE")
    print("1. Play a word")
    print("2. Swap letters")
    print("3. Pass your turn")
    opt = input("CHOOSE MOVE: ")
    if opt == "1":
        pos = input("Position: ")
        direction = input("Horizontal or Vertical (h/v): ")
        word = input("Word: ")
        board.place_letters()
    if opt == "2":
        pass
    if opt == "3":
        pass


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
            options(board, bag)
            











if __name__ == "__main__":
    main()