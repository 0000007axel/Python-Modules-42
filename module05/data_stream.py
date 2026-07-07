from abc import abstractmethod, ABC
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.ingested: list[Any] = []
        self.ingested_count: int = 0
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        outp = (self.rank, str(self.ingested[0]))
        self.rank += 1
        self.ingested.pop(0)
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
                self.ingested.append(data)
            elif isinstance(data, list):
                self.ingested_count += len(data)
                for element in data:
                    self.ingested.append(element)
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
                self.ingested.append(str(data))
            elif isinstance(data, list):
                self.ingested_count += len(data)
                for element in data:
                    self.ingested.append(str(element))
        else:
            raise ValueError("Got exception: Improper numeric data")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for key, value in data.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    return False
            return True
        elif isinstance(data, list):
            for element in data:
                if isinstance(element, dict):
                    for key, value in element.items():
                        if not isinstance(key, str) or not isinstance(value, str):
                            return False
                else:
                    return False
            return True
        else:
            return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if self.validate(data):
            if isinstance(data, dict):
                self.ingested_count += 1
                self.ingested.append(f"{data['log_level']}: {data['log_message']}")
            elif isinstance(data, list):
                self.ingested_count += len(data)
                for d in data:
                    self.ingested.append(f"{d['log_level']}: {d['log_message']}")
        else:
            raise ValueError("Got exception: Improper log data")


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []
        self.ingested_count: int = 0

    def register_processor(self, proc: DataProcessor) -> None:
        if isinstance(proc, DataProcessor):
            self.processors.append(proc)

    def process_stream(self, stream: list[Any]):
        for data in stream:
            for processor in self.processors:
                if processor.validate(data):
                    processor.ingest(data)
                    break 
            else:
                print(f"DataStream error - Can't process element in stream: {data}")

    def print_processors_stats(self) -> None:
        ...



def main() -> None:
    ...

if __name__ == "__main__":
    main()
