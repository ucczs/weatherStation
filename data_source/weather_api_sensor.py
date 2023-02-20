from data_source.dataSourceInterface import DataSource
import requests
import time

class WeatherApi(DataSource):
    api_request = "http://api.weatherapi.com/v1/current.json?key={api}&q={city}&aqi=yes"
    durability_ms = 30000

    def __init__(self, api_key: str, sensor_name: str, city: str) -> None:
        self.api_key = api_key
        self.sensor_name = sensor_name
        self.city = city
        self.timestampLatestMeasurement = -1
        self.latestHumidity = -99
        self.latestTemperature = -99

    def getTemperature(self) -> float:
        time_ms = round(time.time()*1000)
        # get new data via api call
        if ((time_ms - self.timestampLatestMeasurement) > WeatherApi.durability_ms):
            self._getDataViaApi()
        return self.latestTemperature

    def getHumidity(self)-> float:
        time_ms = round(time.time()*1000)
        # get new data via api call
        if ((time_ms - self.timestampLatestMeasurement) > WeatherApi.durability_ms):
            self._getDataViaApi()
        return self.latestHumidity

    def getSensorName(self) -> str:
        return self.sensor_name

    def _getApiRequestString(self) -> str:
        api_request_cust = WeatherApi.api_request.replace("{api}", self.api_key)
        api_request_cust = api_request_cust.replace("{city}", self.city)
        return api_request_cust

    def _getDataViaApi(self) -> None:
        request = self._getApiRequestString()
        response = requests.get(request)
        if response.ok:
            data = response.json()
            self.latestTemperature = data["current"]["temp_c"]
            self.latestHumidity = data["current"]["humidity"]
            self.timestampLatestMeasurement = round(time.time()*1000)
        else:
            self.latestHumidity = -99
            self.latestTemperature = -99
