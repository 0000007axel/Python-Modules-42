import sys


if __name__ == "__main__":
    if sys.prefix != sys.base_prefix:
        print("In a virtual environment")
    print("In a regular environment")
