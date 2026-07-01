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
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            for element in data:
                if not isinstance(element, str):
                    return False
            return True
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data):
            if isinstance(data, str):
                self.ingested_count += 1
                self.ingested_data.append(data)
            elif isinstance(data, list):
                self.ingested_count += len(data)
                for element in data:
                    self.ingested_data.append(element)
        else:
            raise ValueError("Got exception: Improper textual data")


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, int):
            return True
        if isinstance(data, float):
            return True
        elif isinstance(data, list):
            for element in data:
                if not isinstance(element, int) and not isinstance(element, float):
                    return False
            return True
        else:
            return False

    def ingest(self, data: int | float | list[int | float] | list[int] | list[float]) -> None:
        if self.validate(data):
            if isinstance(data, int) or isinstance(data, float):
                self.ingested_count += 1
                self.ingested_data.append(str(data))
            elif isinstance(data, list):
                self.ingested_count += len(data)
                for element in data:
                    self.ingested_data.append(str(element))
        else:
            raise ValueError("Got exception: Improper numeric data")
    
#Still need to make the validation first before ingestion

def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    n = NumericProcessor()
    t = TextProcessor()
    numbers: list[int] = [1, 2, 3, 4, 5]
    words: list[str] = ["Hello", "Nexus", "World"]
    print(f"""Trying to validate input '42': {n.validate(42)}
Trying to validate input 'Hello': {n.validate("Hello")}
Test invalid ingestion of string 'foo' without prior validation:""")
    try:
        n.ingest("foo")
    except ValueError as e:
        print(e)
    print(f"""Processing data: {numbers}
Extracting 3 values...""")
    n.ingest(numbers)
    for i in range(3):
        rank, value = n.output()
        print(f"Numeric value {rank}: {value}")
    print(f"""\n
Testing Text Processor...
Trying to validate input '42': {t.validate(42)}
Processing data: {words}
Extracting 1 value...""")
    t.ingest(words)
    t_rank, t_value = t.output()
    print(f"Text value {t_rank}: {t_value}")


if __name__ == "__main__":
    main()
