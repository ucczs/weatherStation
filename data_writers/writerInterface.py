from abc import ABC, abstractmethod

class DataWriter(ABC):
    @abstractmethod
    def writeData(self, data: str) -> None:
        pass
