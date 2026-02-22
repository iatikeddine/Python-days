def ft_analytics_dashboard() -> None:
    players = [
        {"name": "alice",   "score": 2300, "active": True,  "region": "north",   "achievements": ["first_kill", "level_10", "boss_slayer", "speed_demon", "collector"]},
        {"name": "bob",     "score": 1800, "active": True,  "region": "east",    "achievements": ["first_kill", "level_10", "collector"]},
        {"name": "charlie", "score": 2150, "active": True,  "region": "central", "achievements": ["first_kill", "level_10", "boss_slayer", "speed_demon", "collector", "perfectionist", "treasure_hunter"]},
        {"name": "diana",   "score": 2050, "active": False, "region": "north",   "achievements": ["first_kill", "level_10", "boss_slayer", "treasure_hunter"]},
    ]

    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")
    high_scorers = [p["name"] for p in players if p["score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [p["score"] * 2 for p in players]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [p["name"] for p in players if p["active"]]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores = {p["name"]: p["score"] for p in players}
    print(f"Player scores: {player_scores}")

    score_categories = {
        "high":   len([p for p in players if p["score"] >= 2200]),
        "medium": len([p for p in players if 1900 <= p["score"] < 2200]),
        "low":    len([p for p in players if p["score"] < 1900]),
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {p["name"]: len(p["achievements"]) for p in players}
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")
    unique_players = {p["name"] for p in players}
    print(f"Unique players: {unique_players}")

    unique_achievements = {a for p in players for a in p["achievements"]}
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {p["region"] for p in players if p["active"]}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    total_players = len(players)
    print(f"Total players: {total_players}")

    total_unique_achievements = len(unique_achievements)
    print(f"Total unique achievements: {total_unique_achievements}")

    scores = [p["score"] for p in players]
    average_score = sum(scores) / len(scores)
    print(f"Average score: {average_score}")

    top = max(players, key=lambda p: p["score"])
    print(f"Top performer: {top['name']} ({top['score']} points, {len(top['achievements'])} achievements)")


if __name__ == "__main__":
    ft_analytics_dashboard()
