from dataPreprocessor.preprocessingInterface import DataPreprocessor
import pandas as pd
import numpy as np
import sys

class DataAugmentator(DataPreprocessor):
    invalid_val = -99

    def __init__(self, filter_factor: int, sensor_count: int) -> None:
        self.filter_factor: int = filter_factor
        self.sensor_data: list[pd.DataFrame] = []
        self.sensor_count = sensor_count

    def _removeIncompleteSet(self) -> None:
        pass

    def preprocessData(self, raw_data: pd.DataFrame) -> None:
        if self.sensor_data == []:
            raw_data = raw_data.replace(DataAugmentator.invalid_val, np.nan)

            expected_numb = 0
            for index, row in enumerate(raw_data.iterrows(), 1):
                if int(row[1].sensor_id) == expected_numb:
                    expected_numb = (expected_numb + 1) % 3
                else:
                    found = False
                    i = 1
                    while(not found):
                        if int(raw_data.loc[[index-i]]["sensor_id"]) == 0:
                            found = True
                        raw_data.drop(index=index-i, inplace=True)
                        i += 1

            for sensor_id in range(self.sensor_count):
                data = raw_data[raw_data["sensor_id"] == sensor_id]
                data = data.iloc[::self.filter_factor]
                data = data.fillna(method='ffill')
                self.sensor_data.append(data)
        else:
            sys.exit(-1)

    def getDataSensorID(self, sensor_id: int) -> pd.DataFrame:
        return self.sensor_data[sensor_id]


