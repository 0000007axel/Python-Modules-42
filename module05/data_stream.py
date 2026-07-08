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

    def register_processor(self, proc: DataProcessor) -> None:
        if isinstance(proc, DataProcessor):
            self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            for processor in self.processors:
                if processor.validate(data):
                    processor.ingest(data)
                    break 
            else:
                print(f"DataStream error - Can't process element in stream: {data}")

    def print_processors_stats(self) -> None:
        if not self.processors:
            print("No processors found, no data")
        else:
            for processor in self.processors:
                print(f"{type(processor).__name__}:"
                      f"total {processor.ingested_count} items processed, remaining {len(processor.ingested)} on processor")



def main() -> None:
    d: DataStream = DataStream()
    print(f"""=== Code Nexus - Data Stream ===

Initialize Data Stream...
== Data Stream Statistics ==""")
    d.print_processors_stats()
    data_list: list[Any] = ['Hello world', [3.14, -1, 2.71],
                            [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'},
                             {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
                             42, ['Hi', 'five']]
    print(f"""
Registering Numeric Processor

Send first batch of data on stream: {data_list}""")
    np: NumericProcessor = NumericProcessor()
    d.register_processor(np)
    d.process_stream(data_list)

if __name__ == "__main__":
    main()
