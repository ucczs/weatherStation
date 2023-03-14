from abc import ABC, abstractmethod

class DataReader(ABC):
    @abstractmethod
    def __init__(self, data_path: str) -> None:
        pass

    @abstractmethod
    def getRawData(self, data_path: str):
        pass
