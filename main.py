from data_collector import DataCollector
from data_writers.csv_writer import CsvWriter
from sensors.sensor_dht11 import Sensor_DHT11


def startWeatherTracking():
    output_dir = "/home/pi/weatherScripts/data/"
    file_limit = 1000
    csv_writer = CsvWriter(output_dir, file_limit)


    sensor_pin = 4
    sensor = Sensor_DHT11(sensor_pin, "DHT11")

    myDataCollector = DataCollector(csv_writer, sensor)
    myDataCollector.collectData()


if __name__ == "__main__":
    startWeatherTracking()
