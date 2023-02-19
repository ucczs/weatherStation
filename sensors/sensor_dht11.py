import Adafruit_DHT
import time
from sensorInterface import Sensor

class Sensor_DHT11(Sensor):
    def __init__(self, sensor_pin, sensor_name) -> None:
        self.latestTemperature = -99
        self.latestHumidity = -99
        self.timestampLatestMeasurement = -1
        self.durability_ms = 2000
        self.sensor_pin = sensor_pin
        self.sensor_name = sensor_name

    def getTemperature(self) -> float:
        time_ms = round(time.time()*1000)
        if ((time_ms - self.timestampLatestMeasurement) < self.durability_ms):
            return self.latestTemperature
        else:
            self.latestHumidity, self.latestTemperature = Adafruit_DHT.read(Adafruit_DHT.DHT11, self.sensor_pin)
            self.timestampLatestMeasurement = time_ms
            return self.latestTemperature

    def getHumidity(self) -> float:
        time_ms = round(time.time()*1000)
        if ((time_ms - self.timestampLatestMeasurement) < self.durability_ms):
            return self.latestHumidity
        else:
            self.latestHumidity, self.latestTemperature = Adafruit_DHT.read(Adafruit_DHT.DHT11, self.sensor_pin)
            self.timestampLatestMeasurement = time_ms
            return self.latestHumidity

    def getSensorName(self) -> str:
        return self.sensor_name