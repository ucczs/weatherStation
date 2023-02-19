from data_collector import DataCollector
from data_writers.csv_writer import CsvWriter
from data_writers.console_writer import consoleWriter
from sensors.dummy_sensor import Sensor_Dummy
from sensors.weather_api_sensor import WeatherApi

def dummySensorConsolePrint():
    writer1 = consoleWriter()

    output_dir = "C:\\Users\\odl90\\docs\\GitHub\\weatherStation\\data\\"
    file_limit = 1000
    writer2 = CsvWriter(output_dir, file_limit)

    sensor1 = WeatherApi("", "api sensor", "Stuttgart")
    sensor2 = Sensor_Dummy([-10, 30], [25, 75], "Dummy Sensor 2")

    dataCollector = DataCollector([writer1, writer2], [sensor1, sensor2], 1)
    dataCollector.collectData()

if __name__ == "__main__":
    dummySensorConsolePrint()
