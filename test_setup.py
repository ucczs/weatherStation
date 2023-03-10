from data_collector import DataCollector
from data_sink.csv_writer import CsvWriter
from data_sink.console_writer import consoleWriter
from data_source.dummy_sensor import Sensor_Dummy
from data_source.weather_api_sensor import WeatherApi

def dummySensorConsolePrint():
    writer1 = consoleWriter()

    output_dir = "C:\\Users\\odl90\\docs\\GitHub\\weatherStation\\data\\"
    file_limit = 1000
    writer2 = CsvWriter(output_dir, file_limit)

    sensor1 = WeatherApi("", "api sensor", "Stuttgart")
    sensor2 = Sensor_Dummy([-10, 30], [25, 75], "Dummy Sensor 2")

    time_sync = True
    dataCollector = DataCollector([writer1, writer2], [sensor1, sensor2], 1, time_sync)
    dataCollector.collectData()

def simpleSetup():
    writer1 = consoleWriter()

    output_dir = "C:\\Users\\odl90\\docs\\GitHub\\weatherStation\\data\\"
    file_limit = 1000
    writer2 = CsvWriter(output_dir, file_limit)

    sensor2 = Sensor_Dummy([-10, 30], [25, 75], "Dummy Sensor 2")

    time_sync = True
    dataCollector = DataCollector([writer1, writer2], [sensor2], 1, time_sync)
    dataCollector.collectData()

if __name__ == "__main__":
    dummySensorConsolePrint()
    # simpleSetup()
