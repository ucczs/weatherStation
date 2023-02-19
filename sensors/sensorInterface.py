from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def getTemperature(self):
        pass

    @abstractmethod
    def getHumidity(self):
        pass

    @abstractmethod
    def getSensorName(self):
        pass