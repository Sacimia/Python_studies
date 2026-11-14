
import random

options = ["rock", "paper", "scissor"]

win = {
    "rock": "scissor",
    "paper": "rock",
    "scissor": "paper",
}

emojis = {
    "rock": "✊",
    "paper": "✋",
    "scissor": "✌️"
}

ways = {
    "1": "rock", "r": "rock", "rock": "rock",
    "2": "paper", "p": "paper", "paper": "paper",
    "3": "scissor", "s": "scissor", "scissor": "scissor",
}


def choice_player():
    while True:
        text = input(
            "\nYour turn [1] Rock [2] Paper [3] Scissor [c] Close: "
        ).strip().lower()

        if text in ("c", "close"):
            return None

        if text in ways:
            return ways[text]

        print("Wrong decision! Type 1, 2, 3 or c.")


def choice_computer():
    return random.choice(options)


def results(player, computer):
    if player == computer:
        return "draw"

    if win[player] == computer:
        return "win"

    return "lose"


def show_points(points):
    print("\n" + "=" * 40)
    print("             SCOREBOARD")
    print("=" * 40)
    print(f"Player wins:  {points['win']}")
    print(f"Computer wins: {points['lose']}")
    print(f"Draws:        {points['draw']}")
    print("=" * 40)


def play_round(points):
    player = choice_player()

    if player is None:
        return False

    computer = choice_computer()

    print("\n" + "-" * 40)
    print(f"You:      {emojis[player]} {player}")
    print(f"Computer: {emojis[computer]} {computer}")
    print("-" * 40)

    result = results(player, computer)

    if result == "win":
        print("Congratulations! You win!")
    elif result == "lose":
        print("The computer wins!")
    else:
        print("It's a draw!")

    points[result] += 1

    show_points(points)

    return True


def main():
    points = {
        "win": 0,
        "lose": 0,
        "draw": 0
    }

    print("=" * 40)
    print("       ROCK, PAPER OR SCISSOR")
    print("=" * 40)

    print("\nRules:")
    print("Rock wins scissor.")
    print("Scissor wins paper.")
    print("Paper wins rock.")

    while True:
        if not play_round(points):
            break

    print("\n" + "=" * 40)
    print("             GAME OVER")
    print("=" * 40)

    show_points(points)

    print("\nThanks for playing!")


if __name__ == "__main__":
    main()
