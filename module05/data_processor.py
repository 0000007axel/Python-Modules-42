import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self, data: list[int | float | list[int | float]]) -> None:
        


class TextProcessor(DataProcessor):
    ...

class NumericProcessor(DataProcessor):
    ...

class LogProcessor(DataProcessor):
    ...
