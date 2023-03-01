from abc import ABC, abstractmethod

class DataSink(ABC):
    @abstractmethod
    def writeData(self, data: list[str], time: str = None) -> None:
        pass
