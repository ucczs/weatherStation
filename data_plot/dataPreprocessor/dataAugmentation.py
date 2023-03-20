from dataPreprocessor.preprocessingInterface import DataPreprocessor
import pandas as pd
import numpy as np
import sys

class DataAugmentator(DataPreprocessor):
    invalid_val = -99

    def __init__(self, filter_factor: int, sensor_count: int, max_samples: int = None) -> None:
        self.filter_factor: int = filter_factor
        self.sensor_data: list[pd.DataFrame] = []
        self.sensor_count = sensor_count
        self.max_samples = max_samples

    def _filterIncompleteSets(self, raw_data) -> pd.DataFrame:
        expected_numb = 0

        # remove very first elements if sensor 0 doesn't start
        while(int(raw_data.loc[[0]]["sensor_id"]) != 0):
            raw_data.drop(index=0, inplace=True)
            raw_data.reset_index(drop=True, inplace=True)

        # remove gaps in between
        for index, row in enumerate(raw_data.iterrows(), 1):
            if int(row[1].sensor_id) == expected_numb:
                expected_numb = (expected_numb + 1) % self.sensor_count
            else:
                found = False
                i = 1
                while(not found):
                    if int(raw_data.loc[[index-i]]["sensor_id"]) == 0:
                        found = True
                    raw_data.drop(index=index-i, inplace=True)
                    i += 1

        # make sure that last set is complete
        while(int(raw_data.loc[[raw_data.last_valid_index()]]["sensor_id"]) != (self.sensor_count - 1)):
            raw_data.drop(index=raw_data.last_valid_index(), inplace=True)
            raw_data.reset_index(drop=True, inplace=True)

        return raw_data

    def preprocessData(self, raw_data: pd.DataFrame) -> None:
        if self.sensor_data == []:
            raw_data = raw_data.replace(DataAugmentator.invalid_val, np.nan)

            if self.max_samples is not None:
                raw_data = raw_data.tail(self.max_samples * self.sensor_count + 1)
                raw_data.reset_index(inplace=True)

            raw_data = self._filterIncompleteSets(raw_data)

            for sensor_id in range(self.sensor_count):
                data = raw_data[raw_data["sensor_id"] == sensor_id]
                data = data.iloc[::self.filter_factor]
                data = data.fillna(method='ffill')
                self.sensor_data.append(data)

        else:
            sys.exit(-1)

    def getDataSensorID(self, sensor_id: int) -> pd.DataFrame:
        return self.sensor_data[sensor_id]


