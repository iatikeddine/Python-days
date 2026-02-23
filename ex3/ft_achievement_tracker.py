def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")

    try:
        alice = set(("first_kill", "level_10", "treasure_hunter",
                     "speed_demon"))
    except TypeError as e:
        print(f"Error: {e}")
        alice = set()

    try:
        bob = set(("first_kill", "level_10", "boss_slayer", "collector"))
    except TypeError as e:
        print(f"Error: {e}")
        bob = set()

    try:
        charlie = set((
            "level_10", "treasure_hunter", "boss_slayer",
            "speed_demon", "perfectionist"))
    except TypeError as e:
        print(f"Error: {e}")
        charlie = set()

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    unique = alice.union(bob, charlie)
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}")

    print()
    common = alice.intersection(bob, charlie)
    print(f"Common to all players: {common}")
    charlie_rare = charlie.difference(bob, alice)
    bob_rare = bob.difference(charlie, alice)
    alice_rare = alice.difference(bob, charlie)
    rare = charlie_rare.union(alice_rare, bob_rare)
    print(f"Rare achievements (1 player): {rare}")

    print()
    dif_alice_bob = alice.intersection(bob)
    print(f"Alice vs Bob common: {dif_alice_bob}")
    alice_unique = alice.difference(bob)
    print(f"Alice unique: {alice_unique}")
    bob_unique = bob.difference(alice)
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    ft_achievement_tracker()
