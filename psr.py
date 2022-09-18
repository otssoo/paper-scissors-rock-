import random

option = ["scissors", "rock", "paper"]
pc_choice = random.choice(option)
pc_points = []
player_points = []
game_lenght = 10




def game(player):
    if player == pc_choice:
        print("Tie!")

    elif player == str("rock") and pc_choice == str('scissors') or player == str("paper") and pc_choice == str(
            'rock') or player == str("scissors") and pc_choice == str('paper'):
        print("Win!")

        player_points.append(1)
    else:
        print("You lose!")

        pc_points.append(1)

def program():
    for i in range(game_lenght):
        player = input("Enter your choice:  ").lower()
        game(player)
        print('PC chose is:', pc_choice)
        print('Player:', len(player_points))
        print('PC:', len(pc_points))

program()