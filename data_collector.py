import time
import datetime
from data_source.dataSourceInterface import DataSource
from data_sink.sinkInterface import DataSink

class DataCollector():
    def __init__(self, data_sink: list[DataSink], sensors: list[DataSource], update_time_sec: float, time_sync: bool) -> None:
        self.data_sink = data_sink
        self.sensors = sensors
        self.update_time_sec = update_time_sec
        self.time_sync = time_sync

    def collectData(self) -> None:
        while True:

            if self.time_sync:
                currentTime = str(datetime.datetime.now())
            else:
                currentTime = None

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

                for data_writer in self.data_sink:
                    data_writer.writeData(data_strings, time=currentTime)
            time.sleep(self.update_time_sec)
