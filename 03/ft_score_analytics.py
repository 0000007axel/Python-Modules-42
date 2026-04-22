import sys


def create_list() -> list[int]:
    scores: list[int] = []
    for i in range(0, len(sys.argv) - 1):
        try:
            scores.append(int(sys.argv[i + 1]))
        except ValueError as err:
            print(f"Invalid parameter: '{sys.argv[i + 1]}'")
    if len(scores) > 0:
        print(f"Scores processed: {scores}")
    else:
        print("No scores provided. ", end="") 
        print("Usage: python3 ft_score_analytics.py, <score1> <score2> ...")
    return scores


def get_infos(scores: list[int]) -> None:
    if len(scores) > 0:
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


def main() -> None:
    print("=== Player Score Analytics ===")
    get_infos(create_list())


if __name__ == "__main__":
    main()
