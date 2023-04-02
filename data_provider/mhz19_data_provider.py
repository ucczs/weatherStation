from data_provider.data_provider import DataProvider
from data_provider.sensors.sensor_mh_z19 import Sensor_MH_Z19

class DataProvider_mhz19(DataProvider):
    valid_sensor_types = [
        "co2"
    ]

    def __init__(self, sensor_name: str, sensor_type: str, sensor_instance: Sensor_MH_Z19) -> None:
        if sensor_type not in DataProvider_mhz19.valid_sensor_types:
            raise ValueError("value type for sensor mh_z19 not available: "+ sensor_type)

        super(DataProvider_mhz19, self).__init__(sensor_name, sensor_type)
        self.sensor_instance = sensor_instance

    def getSensorValue(self) -> float:
        return self.sensor_instance.getCo2Value()

