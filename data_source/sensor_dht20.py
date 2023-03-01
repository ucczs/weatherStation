import time
from data_source.dataSourceInterface import DataSource
import smbus2

class Sensor_DHT20(DataSource):
    durability_ms = 2000

    def __init__(self, i2c_adress, sensor_name) -> None:
        self.latestTemperature = -99
        self.latestHumidity = -99
        self.timestampLatestMeasurement = -1
        self.i2c_adress = i2c_adress
        self.i2c_bus = None
        self.sensor_name = sensor_name
        self._init_i2c()

    def _init_i2c(self) -> bool:
        self.i2c_bus = smbus2.SMBus(1)
        data = self.i2c_bus.read_i2c_block_data(self.i2c_adress, 0x71, 1)
        if (data[0] | 0x08) == 0:
            print('[DHT20 sensor] I2C error: Initialization error')

    def _readData(self) -> tuple[float, float]:
        self.i2c_bus.write_i2c_block_data(self.i2c_adress, 0xac, [0x33, 0x00])
        time.sleep(0.1)

        data = self.i2c_bus.read_i2c_block_data(self.i2c_adress, 0x71, 7)

        Traw = ((data[3] & 0xf) << 16) + (data[4] << 8) + data[5]
        temperature = round(200*float(Traw)/2**20 - 50,1)

        Hraw = ((data[3] & 0xf0) >> 4) + (data[1] << 12) + (data[2] << 4)
        humidity = round(100*float(Hraw)/2**20,1)

        return (humidity, temperature)

    def getTemperature(self) -> float:
        time_ms = round(time.time()*1000)
        if ((time_ms - self.timestampLatestMeasurement) < Sensor_DHT20.durability_ms):
            return self.latestTemperature
        else:
            self.latestHumidity, self.latestTemperature = self._readData()
            self.timestampLatestMeasurement = time_ms
            return self.latestTemperature

    def getHumidity(self) -> float:
        time_ms = round(time.time()*1000)
        if ((time_ms - self.timestampLatestMeasurement) < Sensor_DHT20.durability_ms):
            return self.latestHumidity
        else:
            self.latestHumidity, self.latestTemperature = self._readData()
            self.timestampLatestMeasurement = time_ms
            return self.latestHumidity

    def getSensorName(self) -> str:
        return self.sensor_name