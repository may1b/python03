import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
               'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players}")

    capitalized = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {capitalized}")

    only_cap = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {only_cap}")

    scores = {name: random.randint(0, 1000) for name in capitalized}
    print(f"Score dict: {scores}")

    average = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {average}")

    high = {name: score for name, score in scores.items() if score > average}
    print(f"High scores: {high}")


if __name__ == "__main__":
    main()
