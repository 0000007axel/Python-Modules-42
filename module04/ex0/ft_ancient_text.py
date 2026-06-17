import sys
import typing


def reader() -> None:
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        file: typing.IO[str] = open(sys.argv[1], "r")
        print(f"""---

{file.read()}
---
File '{sys.argv[1]}' closed.""")
        file.close()
    except (FileNotFoundError,
            IsADirectoryError,
            PermissionError) as e:
        print(f"Error on opening file '{sys.argv[1]}': {e}")


def main() -> None:
    print("=== Cyber Archives Recovery ===")
    reader()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        main()
