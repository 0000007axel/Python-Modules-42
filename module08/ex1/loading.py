import pandas
import matplotlib
import numpy
import sys


def import_checker(modules: list[str]) -> bool:
    for module in modules:
        if module not in sys.modules:
            print(f"Module '{module}' not loaded.")
        else:
            print(f"")

if __name__ == "__main__":
    print(f"""
LOADING STATUS: Loading Programs...

CHECKING DEPENDENCIES:
          """)
