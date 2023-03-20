import pandas as pd
import matplotlib.pyplot as plt
from dataReader.csvReader import csvReader
from dataPreprocessor.dataAugmentation import DataAugmentator

data_path = "..\\data\\Test02\\"
nth = 2

csv_reader = csvReader(data_path)
df = csv_reader.getRawData()

preprocessor = DataAugmentator(nth, sensor_count=3, max_samples=None)
preprocessor.preprocessData(df)

df_outdoor = preprocessor.getDataSensorID(0)
df_indoor = preprocessor.getDataSensorID(2)

df_dateOnly = pd.to_datetime(df_outdoor["time"]).dt.date
dayChangeList_outdoor = df_dateOnly[df_dateOnly.diff() != "0 days"].index.tolist()

plt.figure("Temperature")
plt.plot(df_outdoor["time"], df_outdoor["temp"], marker=".")
plt.plot(df_indoor["time"], df_indoor["temp"], marker=".")
plt.title("Temperature")
for day in dayChangeList_outdoor[1:]:
    plt.axvline(x = df_outdoor["time"].loc[day], color = 'k', label = 'axvline - full height')

plt.gca().xaxis.set_major_locator(plt.MaxNLocator(5))
plt.gca().axes.set_xlabel("Date (CET)")
plt.gca().axes.set_ylabel("Temprature in °C")
plt.gca().axes.set_ylim(-5,25)


########################################################################

plt.figure("Humidity")
plt.plot(df_outdoor["time"], df_outdoor["humidity"], marker=".")
plt.plot(df_indoor["time"], df_indoor["humidity"], marker=".")
plt.title("Humidity")
for day in dayChangeList_outdoor[1:]:
    plt.axvline(x = df_outdoor["time"].loc[day], color = 'k', label = 'axvline - full height')

plt.gca().xaxis.set_major_locator(plt.MaxNLocator(5))
plt.gca().axes.set_xlabel("Date (CET)")
plt.gca().axes.set_ylabel("Humidity in %")
plt.gca().axes.set_ylim(-5,105)

plt.show()
