from abc import ABC, abstractmethod

class DataProvider(ABC):
    def __init__(self, sensor_name: str, sensor_type: str):
        self.sensor_name: str = sensor_name
        self.sensor_type: str = sensor_type

    def getSensorName(self) -> str:
        return self.sensor_name

    def getSensorType(self) -> str:
        return self.sensor_type

    @abstractmethod
    def getSensorValue(self) -> float:
        pass
