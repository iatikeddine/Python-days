from typing import Generator


def game_event_generator(total: int) -> Generator:
    try:
        int(total)
        players = ["alice", "bob", "charlie"]
        events = ["killed monster", "found treasure", "leveled up"]
        for i in range(total):
            player = players[i % len(players)]
            event = events[i % len(events)]
            level = (i % 20) + 1
            yield (i + 1, player, level, event)
    except (ValueError , TypeError ) as e:
        print(e)
        return

def fibonacci_generator() -> Generator:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_generator() -> Generator:
    n = 2
    while True:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 1


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")
    print("Processing 1000 game events...\n")

    total_events = 1000
    high_level = 0
    treasure_events = 0
    levelup_events = 0

    for event_id, player, level, event in game_event_generator(total_events):
        if event_id <= 3:
            print(f"Event {event_id}: Player {player} (level {level}) {event}")
        if event_id == 4:
            print("...\n")
        if level >= 10:
            high_level += 1
        if event == "found treasure":
            treasure_events += 1
        if event == "leveled up":
            levelup_events += 1

    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {levelup_events}")
    print(f"Memory usage: Constant (streaming)")

    print("\n=== Generator Demonstration ===")

    fib = fibonacci_generator()
    fib_values = []
    for x in range(10):
        fib_values.append(next(fib))
    print(f"Fibonacci sequence (first 10): {fib_values}")

    primes = prime_generator()
    prime_values = []
    for x in range(5):
        prime_values.append(next(primes))
    print(f"Prime numbers (first 5): {prime_values}")


if __name__ == "__main__":
    ft_data_stream()