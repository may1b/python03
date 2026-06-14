import random

achievements = [
    'Crafting Genius',   'World Savior',       'Master Explorer',
    'Collector Supreme', 'Untouchable',        'Boss Slayer',
    'Strategist',        'Unstoppable',        'Speed Runner',
    'Survivor',          'Treasure Hunter',    'First Steps',
    'Sharp Mind',        'Hidden Path Finder', 'Dragon Slayer',
    'Night Owl',         'Perfectionist',      'Legend',
    'The Chosen One',    'Iron Will',
]


def gen_player_achievements() -> set[str]:
    count = random.randint(5, 12)
    return set(random.sample(achievements, count))


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    players = {
        'Alice':   gen_player_achievements(),
        'Bob':     gen_player_achievements(),
        'Charlie': gen_player_achievements(),
        'Dylan':   gen_player_achievements(),
    }

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")
    common = set.intersection(*players.values())
    print(f"Common achievements: {common}")

    print()

    all_achievements = set.union(*players.values())
    print(f"All distinct achievements: {all_achievements}")

    for name, achievements in players.items():
        others_union = set.union(
            *(ach for pname, ach in players.items() if pname != name)
        )
        unique = achievements.difference(others_union)
        print(f"Only {name} has: {unique}")

    print()

    # --- Achievements a player still needs to complete the full list ---
    # all_achievements is the union of what everyone actually unlocked,
    # NOT the full ACHIEVEMENTS pool — matching the expected output.
    for name, achievements in players.items():
        missing = all_achievements.difference(achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
