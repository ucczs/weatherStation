from data_provider.data_provider import DataProvider
from data_provider.sensors.sensor_dummy import Sensor_dummy

class DataProvider_Dummy(DataProvider):
    def __init__(self, sensor_name: str, sensor_type: str, sensor_instance: Sensor_dummy) -> None:
        super(DataProvider_Dummy, self).__init__(sensor_name, sensor_type)
        self.sensor_instance = sensor_instance

    def getSensorValue(self) -> float:
        return self.sensor_instance.getValue()
