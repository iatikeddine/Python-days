def players_events():
    yield "Event 1: Player alice (level 5) killed monster"
    yield "Event 2: Player bob (level 12) found treasure"
    yield "Event 3: Player charlie (level 8) leveled up"
    yield "..."


def data_stream():
    print("=== Game Data Stream Processor ===\n")

    events = players_events()
    for event in events:
        print(event)


data_stream()
