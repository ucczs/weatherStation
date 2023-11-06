from data_collector import DataCollector
from data_sink.csv_writer import CsvWriter
from data_sink.staticHtml_writer import staticHtmlWriter
from data_sink.mqtt_publisher import mqttPublisher

from data_provider.dht20_data_provider import DataProvider_dht20
from data_provider.mhz19_data_provider import DataProvider_mhz19
from data_provider.api_data_provider import DataProvider_api

from data_provider.sensors.sensor_dht20 import Sensor_DHT20
from data_provider.sensors.sensor_mh_z19 import Sensor_MH_Z19
from data_provider.sensors.weather_api_sensor import WeatherApi

from data_sink.console_writer import consoleWriter


def startWeatherTracking():
    output_dir = "/home/pi/weatherScripts/data/"
    file_limit = 10_000
    csv_writer = CsvWriter(output_dir, file_limit)
    console_writer = consoleWriter()
    html_writer = staticHtmlWriter(file_dir="/home/pi/weatherScripts/html_info")
    mqtt_publisher = mqttPublisher('homeassistant.local', 1883, "sensor/temperature_out", "sensor/temperature_in", "sensor/humidity_in", "sensor/last_data_fetch", "sensor/co2_in", '', '')

    i2c_adress = 0x38
    sensor_dht20 = Sensor_DHT20(i2c_adress, "DHT20")
    sensor_mhz19 = Sensor_MH_Z19("MH-Z19")
    api_source = WeatherApi("", "api sensor", "")

    data_provider_dht20_temp = DataProvider_dht20("DHT20", "temperature", sensor_dht20)
    data_provider_dht20_humidity = DataProvider_dht20("DHT20", "humidity", sensor_dht20)
    data_provider_mhz19 = DataProvider_mhz19("MH-Z19", "co2", sensor_mhz19)
    data_provider_api_temp = DataProvider_api("Weather API", "temperature", api_source)
    data_provider_api_humidity = DataProvider_api("Weather API", "humidity", api_source)

    data_provider_list = [
        data_provider_dht20_temp,
        data_provider_dht20_humidity,
        data_provider_mhz19,
        data_provider_api_temp,
        data_provider_api_humidity
    ]

    data_sink_list = [
        csv_writer,
        console_writer,
        html_writer,
        mqtt_publisher
    ]

    time_sync = True
    data_aquisition_time = 30
    myDataCollector = DataCollector(data_sink_list, data_provider_list, data_aquisition_time, time_sync)
    myDataCollector.collectData()


if __name__ == "__main__":
    startWeatherTracking()
