

import rps
import guess_number


def arcade(name="PlayerOne"):
    print(f"\n{name}, welcome to the Arcade! 🎮\n")
    while True:
        choice = input(
            f"Please choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\nOr press \"X\" to exit the Arcade.\n")

        if choice not in ["1", "2", "X", "x"]:
            print(f"{name}, please enter 1, 2, or X")
            continue

        if choice == "1":
            result = rps.rps(name, arcade=True)
            if result == "Q":
                print(f"\n{name}, welcome back to the Arcade! 🎮\n")

        elif choice == "2":
            result = guess_number.guess_number(name, arcade=True)
            if result == "Q":
                print(f"\n{name}, welcome back to the Arcade! 🎮\n")

        else:
            print(f"\nSee you next time!\n\nBye {name}!👋\n")
            break


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()
    arcade(args.name)
