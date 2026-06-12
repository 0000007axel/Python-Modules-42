#!/usr/bin/env python3.13


import sys


def create_list() -> list[int]:
    scores: list[int] = []
    i = 0
    while i < len(sys.argv) - 1:
        try:
            if int(sys.argv[i + 1]) > 9999999999:
                raise (ValueError("Number too large"))
            scores.append(int(sys.argv[i + 1]))
            i = i + 1
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i + 1]}'")
            i = i + 1
            continue
    if len(scores) > 0:
        print(f"Scores processed: {scores}")
    else:
        print("No scores provided. ", end="")
        print("Usage: python3 ft_score_analytics.py, <score1> <score2> ...")
    return scores


def get_infos(scores: list[int]) -> None:
    if len(scores) > 0:
        print(f"""Total players: {len(scores)}
Total score: {sum(scores)}
Average score: {round(sum(scores) / len(scores), 2)}
High score: {max(scores)}
Low score: {min(scores)}
Score range: {max(scores) - min(scores)}
""")


def main() -> None:
    print("=== Player Score Analytics ===")
    get_infos(create_list())


if __name__ == "__main__":
    main()
