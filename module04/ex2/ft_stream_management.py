import sys
from typing import TextIO


def formater(text: str) -> str:
    print("Transform data\n---\n")
    new_formated_text: str = text.replace("\n", "#\n")
    print(new_formated_text)
    print("\n---")
    return (new_formated_text)


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation===")

    if len(sys.argv) != 2:
        print(f"[STDERR] Usage: {sys.argv[0]} <file>", file=sys.stderr)
        return

    try:
        print(f"Accessing file '{sys.argv[1]}'\n---\n")
        f: TextIO = open(sys.argv[1], "r")
        orig_text: str = f.read()
        print(orig_text)
        f.close()
        print(f"\n---\nFile '{sys.argv[1]}' closed\n")
        new_text: str = formater(orig_text)
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        new_filename: str = sys.stdin.readline().strip()
        if len(new_filename) == 0:
            print("Not saving data")
            return
        else:
            try:
                print(f"Saving data to '{new_filename}'")
                nf: TextIO = open(new_filename, "w")
                nf.write(new_text)
                nf.close()
                print(f"Data saved in file '{new_filename}'")
            except Exception as err:
                print(f"[STDERR] Error opening file {new_filename}: "
                      f"{err}\nData not saved.")
                return
    except Exception as e:
        print(f"[STDERR] Error opening file '{sys.argv[1]}: {e}",
              file=sys.stderr)


if __name__ == "__main__":
    main()
