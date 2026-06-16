import sys
from typing import TextIO


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    try:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        file: str = sys.argv[1]
        f: TextIO = open(file, "r")
        print("---\n")
        print(f.read())
        print("\n---")
        f.close()
        print(f"File '{sys.argv[1]}' closed")
    except Exception as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    main()
