#!/usr/bin/env


from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self, data: list[Any] | Any):
        self.data = data
    
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        ...


class NumericProcessor(DataProcessor):
    def __init__(self, data: Any):
        super().__init__(data)

    def validate(self, data: Any) -> bool:
        ...

    def ingest(self, data: Any) -> None:
        ...


class TextProcessor(DataProcessor):
    ...


class LogProcessor(DataProcessor):
    ...


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing numeric processor...")
    

if __name__ == "__main__":
    main()
