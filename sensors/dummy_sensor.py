from sensors.sensorInterface import Sensor
from random import randint

class Sensor_Dummy(Sensor):
    def __init__(self, temp_range: list[int], humidity_range: list[int], sensor_name: str) -> None:
        self.temp_range = temp_range
        self.humidity_range = humidity_range
        self.sensor_name = sensor_name

    def getTemperature(self) -> int:
        return randint(self.temp_range[0], self.temp_range[1])

    def getHumidity(self) -> int:
        return randint(self.humidity_range[0], self.humidity_range[1])

    def getSensorName(self) -> str:
        return self.sensor_name
