players = [
    {"name": "alice", "score": 2300, "region": "north",
     "achievements": ["first_kill", "level_10", "boss_slayer", "speed_run", "survivor"],
     "active": True},
    {"name": "bob", "score": 1800, "region": "east",
     "achievements": ["first_kill", "level_10", "explorer"],
     "active": True},
    {"name": "charlie", "score": 2150, "region": "central",
     "achievements": ["first_kill", "level_10", "boss_slayer", "speed_run",
                      "survivor", "explorer", "legend"],
     "active": True},
    {"name": "diana", "score": 2050, "region": "north",
     "achievements": ["first_kill", "level_10", "boss_slayer", "explorer"],
     "active": False},
    {"name": "eve", "score": 1500, "region": "east",
     "achievements": ["first_kill", "level_10"],
     "active": False},
    {"name": "frank", "score": 900, "region": "central",
     "achievements": ["first_kill"],
     "active": False},
]

print("=== Game Analytics Dashboard ===")

print("\n=== List Comprehension Examples ===")

high_scorers = [player["name"] for player in players if player["score"] > 2000]
print(f"High scorers (>2000): {high_scorers}")

scores_doubled = [player["score"] * 2 for player in players if player["score"] > 2000]
print(f"Scores doubled: {scores_doubled}")

active_players = [player["name"] for player in players if player["active"]]
print(f"Active players: {active_players}")

print("\n=== Dict Comprehension Examples ===")

player_scores = {player["name"]: player["score"] for player in players}
print(f"Player scores: {player_scores}")


def score_category(score: int) -> None:
    try:
        if score >= 2000:
            return "high"
        elif score >= 1500:
            return "medium"
        return "low"
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


score_categories = {
    cat: len([player for player in players if score_category(player["score"]) == cat])
    for cat in ["high", "medium", "low"]
}
print(f"Score categories: {score_categories}")

achievement_counts = {player["name"]: len(player["achievements"]) for player in players}
print(f"Achievement counts: {achievement_counts}")

print("\n=== Set Comprehension Examples ===")

unique_players = {player["name"] for player in players}
print(f"Unique players: {unique_players}")

unique_achievements = {a for player in players for a in player["achievements"]}
print(f"Unique achievements: {unique_achievements}")

active_regions = {player["region"] for player in players if player["active"]}
print(f"Active regions: {active_regions}")

print("\n=== Combined Analysis ===")

total_players = len(players)
print(f"Total players: {total_players}")

total_unique_achievements = len(unique_achievements)
print(f"Total unique achievements: {total_unique_achievements}")

scores = [player["score"] for player in players]
average_score = sum(scores) / len(scores)
print(f"Average score: {average_score}")

top = sorted([player["score"] for player in players])
print(
    f"Top performer: {top} "
    f"({top['score']} points, {len(top['achievements'])} achievements)"
)
