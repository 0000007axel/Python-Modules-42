from abc import abstractmethod, ABC
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.ingested_data: list[Any] = []
        self.ingested_count: int = 0
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        outp = (self.rank, str(self.ingested_data[0]))
        self.rank += 1
        self.ingested_data.pop(0)
        return outp
        


class TextProcessor(DataProcessor):
    ...

class NumericProcessor(DataProcessor):
    ...

class LogProcessor(DataProcessor):
    ...




def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")


if __name__ == "__main__":
    main()
