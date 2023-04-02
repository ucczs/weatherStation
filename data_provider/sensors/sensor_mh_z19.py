import time
import mh_z19

class Sensor_MH_Z19():
    durability_ms = 2000

    def __init__(self, sensor_name) -> None:
        self.latestCo2 = -99
        self.sensor_name = sensor_name
        self.timestampLatestMeasurement = -1

    def _readData(self):
        return mh_z19.read_co2valueonly()

    def getSensorName(self) -> str:
        return self.sensor_name

    def getCo2Value(self) -> str:
        time_ms = round(time.time()*1000)
        if ((time_ms - self.timestampLatestMeasurement) < Sensor_MH_Z19.durability_ms):
            return self.latestCo2
        else:
            self.latestCo2 = self._readData()
            self.timestampLatestMeasurement = time_ms
            return self.latestCo2

