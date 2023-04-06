from data_provider.data_provider import DataProvider
from data_provider.sensors.weather_api_sensor import WeatherApi

class DataProvider_api(DataProvider):
    valid_sensor_types = [
        "temperature",
        "humidity"
    ]

    def __init__(self, sensor_name: str, sensor_type: str, sensor_instance: WeatherApi) -> None:
        if sensor_type not in DataProvider_api.valid_sensor_types:
            raise ValueError("value type for api sensor not available: "+ sensor_type)

        super(DataProvider_api, self).__init__(sensor_name, sensor_type)
        self.sensor_instance = sensor_instance

    def getSensorValue(self) -> float:
        if self.sensor_type == "temperature":
            return self.sensor_instance.getTemperature()
        elif self.sensor_type == "humidity":
            return self.sensor_instance.getHumidity()
        else:
            raise ValueError("value type for api sensor not available")
