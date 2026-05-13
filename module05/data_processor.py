#!usr/bin/env python3.13


from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self, data) -> None:
        self.data = data

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self) -> None:
        pass

    def output(self, data:Any) -> tuple[int, str]:
        print(data)
        return 


class NumericProcessor(DataProcessor):
    def __init__(self, data: float) -> None:
        self.data = data
        super().__init__(self.data)

    def validate(self, data: float) -> bool:
        state: bool = True
        print(f" Trying to validate input '{self.data}': {state}")

    def ingest(self, data) -> None:
        ...



class TextProcessor(DataProcessor):
    ...

class LogProcessor(DataProcessor):
    ...



def main():
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    num = NumericProcessor(42)



if __name__ == "__main__":
    main()
