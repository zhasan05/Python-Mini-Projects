import random

def player_roll():
    min_value = 1
    max_value = 6
    rand_roll = random.randint(min_value, max_value)
    return rand_roll

def get_total_players():
    while True:
        user_input = input("Enter the no.of players that want to play? Choose between (2-4) only: ").lower()
        if user_input.isdigit():
            num_players = int(user_input)
            if 2 <= num_players <= 4:
                return num_players
            else:
                print("Please choose between (2-4) players!")
        else:
            print("Invalid input! Please try again!")

def get_current_player_score(player_position, total_score):
    #Play one player's turn and return the points earned this turn.
    print(f"\nPlayer {player_position + 1}, your turn has started now\n")
    print(f"Your total score is {total_score}\n")

    current_score = 0

    while True:
        roll_prompt = input("Do you want to roll? Select (y/n) to proceed: ").lower()
        if roll_prompt != 'y':
            print('Ending your turn!')
            break

        value = player_roll()

        if value == 1:
            current_score = 0
            print("You rolled a 1, your turn is now over")
            print(f"Your current score is {current_score}")
            break
        else:
            current_score += value
            print(f"You rolled a {value}")
            print(f"Your current score is {current_score}")

    return current_score

def main():
    print("=== Welcome to PIG ===")

    max_score = 21
    players = get_total_players()
    players_score_list = [0] * players

    while max(players_score_list) < max_score:
        for position in range(players):
            current_player_score = get_current_player_score(position, players_score_list[position])
            players_score_list[position] += current_player_score
            print(f"Player {position + 1} your current score is now {players_score_list[position]}")

            if players_score_list[position] >= max_score:
                break

    winner_position = players_score_list.index(max(players_score_list))
    print(f"Player {winner_position + 1} has won with a total score of {players_score_list[winner_position]}")

if __name__ == "__main__":
    main()
