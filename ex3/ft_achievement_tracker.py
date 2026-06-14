import random

ACHIEVEMENTS = [
    'Crafting Genius',   'World Savior',       'Master Explorer',
    'Collector Supreme', 'Untouchable',        'Boss Slayer',
    'Strategist',        'Unstoppable',        'Speed Runner',
    'Survivor',          'Treasure Hunter',    'First Steps',
    'Sharp Mind',        'Hidden Path Finder', 'Dragon Slayer',
    'Night Owl',         'Perfectionist',      'Legend',
    'The Chosen One',    'Iron Will',          'Puzzle Master',
    'Team Player',       'Lucky Find',         'Marathon Gamer',
    'Secret Keeper',
]


def gen_player_achievements() -> set[str]:
    count = random.randint(10, 12)
    return set(random.sample(ACHIEVEMENTS, count))


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    players = {
        'Alice':   gen_player_achievements(),
        'Bob':     gen_player_achievements(),
        'Charlie': gen_player_achievements(),
        'Dylan':   gen_player_achievements(),
    }

    for name, unlocked in players.items():
        print(f"Player {name}: {unlocked}")
    all_achievements = set.union(*players.values())
    print(f"All distinct achievements: {all_achievements}")

    common = set.intersection(*players.values())
    print(f"Common achievements: {common}")

    for name, unlocked in players.items():
        others_union = set.union(
            *(ach for pname, ach in players.items() if pname != name)
        )
        unique = unlocked.difference(others_union)
        print(f"Only {name} has: {unique}")

    print()

    full_achievement_set = set(ACHIEVEMENTS)
    for name, unlocked in players.items():
        missing = full_achievement_set.difference(unlocked)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
