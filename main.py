from data_collector import DataCollector
from data_sink.csv_writer import CsvWriter
from data_source.sensor_dht11 import Sensor_DHT11
from data_source.weather_api_sensor import WeatherApi


def startWeatherTracking():
    output_dir = "/home/pi/weatherScripts/data/"
    file_limit = 3000
    csv_writer = CsvWriter(output_dir, file_limit)


    sensor_pin = 4
    sensor_1 = Sensor_DHT11(sensor_pin, "DHT11")

    sensor_pin = 5
    sensor_2 = Sensor_DHT11(sensor_pin, "DHT11")

    api_source = WeatherApi("", "api sensor", "Stuttgart")

    myDataCollector = DataCollector([csv_writer], [api_source, sensor_1, sensor_2], 30)
    myDataCollector.collectData()


if __name__ == "__main__":
    startWeatherTracking()
