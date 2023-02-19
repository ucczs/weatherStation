import time
from sensors.sensorInterface import Sensor
from data_writers.writerInterface import DataWriter

class DataCollector():
    def __init__(self, data_writers: list[DataWriter], sensors: list[Sensor], update_time_sec: float) -> None:
        self.data_writers = data_writers
        self.sensors = sensors
        self.update_time_sec = update_time_sec

    def collectData(self) -> None:
        while True:
            for sensor_idx, sensor in enumerate(self.sensors):
                temperature = sensor.getTemperature()
                humidity = sensor.getHumidity()
                if (temperature is None):
                    temperature = -99
                temp_str = "{:f}".format(temperature)

                if (humidity is None):
                    humidity = -99
                humidity_str = "{:f}".format(humidity)

                sensor_name = sensor.getSensorName()
                data_strings = [str(sensor_idx), sensor_name, temp_str, humidity_str]

                for data_writer in self.data_writers:
                    data_writer.writeData(data_strings)
                time.sleep(self.update_time_sec)
