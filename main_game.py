from bag import Bag
from players import Player

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
        

def main():
    #make players
    player_list = create_players()
    #make bag
    bag = Bag()
    end = True
    while end == True:
        for player in player_list:
            #draw letters
            player.hand = bag.draw_letters(player.hand)
        print()










if __name__ == "__main__":
    main()