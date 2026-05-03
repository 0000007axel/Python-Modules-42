#!/usr/bin/env python3.13


import sys


def find_max(scores: list[int]) -> int:
    max_value: int = 0
    for score in scores:
        if score > max_value:
            max_value = score
    return (max_value)


def find_min(scores: list[int]) -> int:
    min_value: int = find_max(scores)
    for score in scores:
        if score < min_value:
            min_value = score
    return (min_value)


def create_list() -> list[int]:
    scores: list[int] = []
    i = 0
    while i < len(sys.argv) - 1:
        try:
            scores.append(int(sys.argv[i + 1]))
            i = i + 1
        except ValueError:
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
        print(f"High score: {find_max(scores)}")
        print(f"Low score: {find_min(scores)}")
        print(f"Score range: {find_max(scores) - find_min(scores)}")


def main() -> None:
    print("=== Player Score Analytics ===")
    get_infos(create_list())


if __name__ == "__main__":
    main()
