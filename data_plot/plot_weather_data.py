import pandas as pd
import matplotlib.pyplot as plt
from dataReader.csvReader import csvReader
from dataPreprocessor.dataAugmentation import DataAugmentator

data_path = "..\\data\\bed_room\\"
nth = 1

csv_reader = csvReader(data_path)
df = csv_reader.getRawData()

preprocessor = DataAugmentator(nth, sensor_count=5, max_samples=None)
preprocessor.preprocessData(df)

dht20_temp = preprocessor.getDataSensorID(0)
dht20_humidity = preprocessor.getDataSensorID(1)
mhz19_co2 = preprocessor.getDataSensorID(2)
api_temp = preprocessor.getDataSensorID(3)
api_humidity = preprocessor.getDataSensorID(4)

df_dateOnly = pd.to_datetime(dht20_temp["time"]).dt.date
dayChangeList = df_dateOnly[df_dateOnly.diff() != "0 days"].index.tolist()

plt.figure("Temperature")
plt.plot(dht20_temp["time"], dht20_temp["sensor_value"], marker=".")
plt.plot(api_temp["time"], api_temp["sensor_value"], marker=".")
plt.title("Temperature")
for day in dayChangeList[1:]:
    plt.axvline(x = dht20_temp["time"].loc[day], color = 'k', label = 'axvline - full height')

plt.gca().xaxis.set_major_locator(plt.MaxNLocator(5))
plt.gca().axes.set_xlabel("Date (CET)")
plt.gca().axes.set_ylabel("Temprature in °C")
plt.gca().axes.set_ylim(-5,25)


########################################################################

df_dateOnly = pd.to_datetime(dht20_humidity["time"]).dt.date
dayChangeList = df_dateOnly[df_dateOnly.diff() != "0 days"].index.tolist()

plt.figure("Humidity")
plt.plot(dht20_humidity["time"], dht20_humidity["sensor_value"], marker=".")
plt.plot(api_humidity["time"], api_humidity["sensor_value"], marker=".")
plt.title("Humidity")
for day in dayChangeList[1:]:
    plt.axvline(x = dht20_humidity["time"].loc[day], color = 'k', label = 'axvline - full height')

plt.gca().xaxis.set_major_locator(plt.MaxNLocator(5))
plt.gca().axes.set_xlabel("Date (CET)")
plt.gca().axes.set_ylabel("Humidity in %")
plt.gca().axes.set_ylim(-5,105)

########################################################################

df_dateOnly = pd.to_datetime(mhz19_co2["time"]).dt.date
dayChangeList = df_dateOnly[df_dateOnly.diff() != "0 days"].index.tolist()

plt.figure("CO2 Concentration")
plt.plot(mhz19_co2["time"], mhz19_co2["sensor_value"], marker=".")
plt.title("CO2 Concentration")
for day in dayChangeList[1:]:
    plt.axvline(x = mhz19_co2["time"].loc[day], color = 'k', label = 'axvline - full height')

plt.gca().xaxis.set_major_locator(plt.MaxNLocator(5))
plt.gca().axes.set_xlabel("Date (CET)")
plt.gca().axes.set_ylabel("Co2 Concentration in ppm")
plt.gca().axes.set_ylim(0,1500)

plt.show()