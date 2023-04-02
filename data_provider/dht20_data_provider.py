from data_provider.data_provider import DataProvider
from data_provider.sensors.sensor_dht20 import Sensor_DHT20

class DataProvider_dht20(DataProvider):
    valid_sensor_types = [
        "temperature",
        "humidity"
    ]

    def __init__(self, sensor_name: str, sensor_type: str, sensor_instance: Sensor_DHT20) -> None:
        if sensor_type not in DataProvider_dht20.valid_sensor_types:
            raise ValueError("value type for sensor dht20 not available: "+ sensor_type)

        super(DataProvider_dht20, self).__init__(sensor_name, sensor_type)
        self.sensor_instance = sensor_instance

    def getSensorValue(self) -> float:
        if self.sensor_type == "temperature":
            return self.sensor_instance.getTemperature()
        elif self.sensor_type == "humidity":
            return self.sensor_instance.getHumidity()
        else:
            raise ValueError("value type for sensor dht20 not available")
