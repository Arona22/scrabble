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
    print("1. Play a word")
    print("2. Swap letters")
    print("3. Pass your turn")
    player.print_hand()
    opt = input("CHOOSE MOVE: ")

    if opt == "1":
        turn = True
        while turn is not None:
            word = input("Word: ").upper()
            pos = input("Position to place from: ").upper()
            direction = input("Horizontal or Vertical (h/v): ").upper()

            turn = board.place_letters(player.hand, word, pos, direction)
            if turn is not None:
                print(turn)
            if turn == f"{word} is not in dictionary. Turn forfeited":
                turn = None


        #take out letters used
        bag.swap(player.hand, word)

        pass_counter = 0
        return pass_counter

    elif opt == "2":
        let_swap = input("What letters to swap? (e.x: AFSAS) ").upper()
        bag.swap(player.hand, let_swap)
        pass_counter = 0
        return pass_counter

    elif opt == "3":
        pass_counter += 1
        return pass_counter


def main():
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
            pass_counter = options(board, bag, player, pass_counter)
            











if __name__ == "__main__":
    main()