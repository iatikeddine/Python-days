print("=== Achievement Tracker System ===")
print()

alice = set(("first_kill", "level_10", "treasure_hunter", "speed_demon"))
bob = set(("first_kill", "level_10", "boss_slayer", "collector"))
charlie = set(("level_10", "treasure_hunter", "boss_slayer",
               "speed_demon", "perfectionist"))

print(f"Player alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}")

print()
print("=== Achievement Analytics ===")
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