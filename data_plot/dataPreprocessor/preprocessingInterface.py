from abc import ABC, abstractmethod
import pandas as pd

class DataPreprocessor(ABC):
    @abstractmethod
    def preprocessData(self, raw_data: pd.DataFrame, sensor_id_online: int, sensor_id_dht11: int, sensor_id_dht20) -> None:
        pass

    @abstractmethod
    def getDataSensorID(self, sensor_id) -> pd.DataFrame:
        pass
