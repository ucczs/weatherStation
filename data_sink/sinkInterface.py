from abc import ABC, abstractmethod

class DataSink(ABC):
    @abstractmethod
    def writeData(self, data: str) -> None:
        pass
