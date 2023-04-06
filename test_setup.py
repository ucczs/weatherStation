from data_sink.console_writer import consoleWriter
from data_provider.dummy_data_provider import DataProvider_Dummy
from data_provider.sensors.sensor_dummy import Sensor_dummy
from data_collector import DataCollector

def dummySensorConsolePrint():
    writer1 = consoleWriter()
    sensor = Sensor_dummy([10, 100])

    sensor_provider_1 = DataProvider_Dummy("Dummy Sensor", "temperature", sensor)
    sensor_provider_2 = DataProvider_Dummy("Dummy Sensor", "humidity", sensor)
    sensor_provider_3 = DataProvider_Dummy("Dummy Sensor", "co2", sensor)

    data_provider_list = [
        sensor_provider_1,
        sensor_provider_2,
        sensor_provider_3
    ]

    time_sync = True
    dataCollector = DataCollector([writer1], data_provider_list, 1, time_sync)
    dataCollector.collectData()

if __name__ == "__main__":
    dummySensorConsolePrint()
