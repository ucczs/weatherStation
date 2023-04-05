from dataReader.dataReaderInterface import DataReader
import pandas as pd
from os import path
from os import walk

class csvReader(DataReader):
    header = ["time", "sensor_id", "sensor_name", "sensor_type", "sensor_value", "NaN"]

    def __init__(self, data_path: str) -> None:
        self.data_path = data_path
        self.filenames = []

    def _isDirectory(self, data_path) -> bool:
        return path.isdir(data_path)
    
    def _readInData(self) -> pd.DataFrame:
        df = pd.DataFrame()
        for file in self.filenames:
            df_single = pd.read_csv(self.data_path + file, names=csvReader.header)
            df_single.set_index("time")
            df_single.dropna(axis=0, how="all", inplace=True)
            df = pd.concat([df, df_single], ignore_index=True)
        return df

    def getRawData(self) -> pd.DataFrame:
        if self._isDirectory(self.data_path):
            self.filenames = next(walk(self.data_path), (None, None, []))[2]  # [] if no file
        else:
            self.filenames = [self.data_path]

        df = self._readInData()
        return df
