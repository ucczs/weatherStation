import time
import datetime
from data_provider.data_provider import DataProvider
from data_sink.sinkInterface import DataSink

class DataCollector():
    def __init__(self, data_sink: list[DataSink], sensor_data_providers: list[DataProvider], update_time_sec: float, time_sync: bool) -> None:
        self.data_sink = data_sink
        self.sensor_data_providers = sensor_data_providers
        self.update_time_sec = update_time_sec
        self.time_sync = time_sync

    def collectData(self) -> None:
        while True:

            if self.time_sync:
                currentTime = str(datetime.datetime.now())
            else:
                currentTime = None

            for sensor_idx, sensor_data_provider in enumerate(self.sensor_data_providers):
                sensor_value = sensor_data_provider.getSensorValue()
                if (sensor_value is None):
                    sensor_value = -99
                sensor_val_str = "{:f}".format(sensor_value)

                sensor_name = sensor_data_provider.getSensorName()
                sensor_type = sensor_data_provider.getSensorType()
                data_strings = [str(sensor_idx), sensor_name, sensor_type, sensor_val_str]

                for data_writer in self.data_sink:
                    data_writer.writeData(data_strings, time=currentTime)

            time.sleep(self.update_time_sec)
