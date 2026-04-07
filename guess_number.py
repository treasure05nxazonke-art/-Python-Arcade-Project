import sys
import random


def guess_number(name="PlayerOne", arcade=False):
    game_count = 0
    player_wins = 0
    winning_percentage = 0

    def play_game():
        nonlocal name
        nonlocal game_count
        nonlocal player_wins
        nonlocal winning_percentage

        playerpicks = (
            input(f"{name}, guess which number l'm thinking of ... 1, 2, or 3.\n"))
        if playerpicks not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.\n")
            return play_game()

        player = int(playerpicks)

        computerpicks = random.randint(1, 3)

        computer = int(computerpicks)

        print(f"{name}, you chose {player}\n")

        print(f"l was thinking about the number {computer}\n")

        def determine_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal game_count

            game_count += 1

            if player == computer:
                player_wins += 1
                return f"🥳 {name}, you win!\n"
            else:
                return f"Sorry, {name}, Better luck next time.😢\n"

        game_points = determine_winner(player, computer)

        winning_percentage = (player_wins / game_count) * 100

        print(game_points)

        print(f"Game count: {game_count}\n")

        print(f"{name}'s wins: {player_wins}\n")

        print(f"Your winning percentage: {winning_percentage:.2f}%\n")

        while True:
            playagain = input(
                f"Play again, {name}?\n \nY for yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                print(f"{name}, please enter Y for yes or Q to quit.\n")
                continue
            if playagain.lower() == "y":
                return play_game()
            else:
                if arcade:
                    print(f"{name}, welcome back to the Arcade! 🎮\n")
                    return "Q"
                else:
                    print("\n🥳🥳🥳🥳")
                    print("Thank you for playing!\n")
                    sys.exit(f"Bye {name}!👋\n")

    play_game()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Provides a personalized guessing game experience.")

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the player."
    )

    args = parser.parse_args()
    guess_number(args.name)
