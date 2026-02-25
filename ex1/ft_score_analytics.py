import sys


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py"
            "<score1> <score2> ..."
        )
    else:
        scores_list = []
        for x in sys.argv[1:]:
            try:
                scores_list.append(int(x))
            except ValueError:
                print(f"oops, I typed {x} instead of number")
        if len(scores_list) == 0:
            print("All inputs are invalid")
        else:
            print(f"Scores processed: {scores_list}")
            print(f"Total players: {len(scores_list)}")
            print(f"Total score: {sum(scores_list)}")
            print(f"Average score: {sum(scores_list) / len(scores_list)}")
            print(f"High score: {max(scores_list)}")
            print(f"Low score: {min(scores_list)}")
            print(f"Score range: {max(scores_list) - min(scores_list)}")


if __name__ == "__main__":
    ft_score_analytics()
