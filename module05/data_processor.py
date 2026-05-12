#!usr/bin/env python3.13


from abc import ABC


class DataProcessor(ABC):
    def __init__(self) -> None:
        processed_data: list[Any] = []


def main() -> None:
    print("=== Garden Data Processor ===")


if __name__ == "__main__":
    main()
