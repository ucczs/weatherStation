from data_collector import DataCollector
from data_sink.csv_writer import CsvWriter
from data_source.sensor_dht11 import Sensor_DHT11
from data_source.sensor_dht20 import Sensor_DHT20
from data_source.weather_api_sensor import WeatherApi
from data_sink.console_writer import consoleWriter


def startWeatherTracking():
    output_dir = "/home/pi/weatherScripts/data/"
    file_limit = 3000
    csv_writer = CsvWriter(output_dir, file_limit)
    writer1 = consoleWriter()

    sensor_pin = 4
    sensor_1 = Sensor_DHT11(sensor_pin, "DHT11")

    i2c_adress = 0x38
    sensor_2 = Sensor_DHT20(i2c_adress, "DHT20")

    api_source = WeatherApi("", "api sensor", "Stuttgart")

    time_sync = True
    data_aquisition_time = 30
    myDataCollector = DataCollector([writer1], [api_source, sensor_1, sensor_2], data_aquisition_time, time_sync)
    myDataCollector.collectData()


if __name__ == "__main__":
    startWeatherTracking()
