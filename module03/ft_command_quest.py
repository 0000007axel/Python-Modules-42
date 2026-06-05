import sys

def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0].split('/')[-1]}" )
    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {len(sys.argv)}")

if __name__ == "__main__":
    main()
