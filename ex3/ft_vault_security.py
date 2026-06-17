import sys
import typing


def reader() -> None:
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        file: typing.IO[str] = open(sys.argv[1], "r")
        file_contents: str = file.read()
        print(f"""---

{file_contents}
---
File '{sys.argv[1]}' closed.\n""")
        file.close()
        new_content: str = file_contents.replace("\n", "#\n")
        print(f"""Transform data:
---

{new_content}
---
""")
        print("Enter new file name (or empty): ", end="", flush=True)
        new_name: str = sys.stdin.readline().rstrip("\n")
        if new_name:
            print(f"Saving data to '{new_name}'")
            try:
                file_w: typing.IO[str] = open(new_name, "w")
                file_w.write(new_content)
                file_w.close()
                print(f"Data saved to '{new_name}'.")
            except (FileNotFoundError,
                    IsADirectoryError,
                    PermissionError) as e:
                print(f"[STDERR] Error on writing in file '{new_name}': {e}",
                      file=sys.stderr)
        else:
            print("Not writing new data.")

    except (FileNotFoundError,
            IsADirectoryError,
            PermissionError) as e:
        print(f"[STDERR] Error on opening file '{sys.argv[1]}': {e}",
              file=sys.stderr)


def main() -> None:
    print("=== Cyber Archives Recovery ===")
    reader()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        try:
            main()
        except (KeyboardInterrupt, EOFError):
            print("\n[STDERR] Program interrupted by user.", file=sys.stderr)
