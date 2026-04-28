import sys


def read_file() -> None:
    try:
        file: str = sys.argv[1]
        print(f"Accessing file '{file}'")
        with open(file) as f:
            print("---\n")
            print(f.read())
            print("---")
        print(f"File '{file}' closed")
    except FileNotFoundError as err1:
        print(f"Error opening file '{file}': {err1}") 
    except PermissionError as err2:
        print(f"Error opening file '{file}': {err2}")
    except IndexError:
        print(f"Usage: {sys.argv[0]} <file>")


def main() -> None:
    print("=== Cyber Archives Recovery ===")
    read_file()


if __name__ == "__main__":
    main()
