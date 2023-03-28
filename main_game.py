from bag import Bag
from players import Player

def create_players():
    player_list = []
    player_count = int(input("How many players are playing? "))
    for i in range(player_count):
        player = Player()
        input_name = input(f"Name of player {i+1}: ")
        player.name = input_name
        player_list.append(player)
    return player_list        
        

def main():
    player_list = create_players()
    for i in len(player_list):
        pass

    print(player_list)






if __name__ == "__main__":
    main()