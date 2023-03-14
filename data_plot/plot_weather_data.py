import pandas as pd
import matplotlib.pyplot as plt
from os import walk

header = ["time", "sensor_id", "sensor_name", "temp", "humidity", "NaN"]
# df = pd.read_csv("../data/data_20230221-220724.csv", names=header)

data_path = "..\\data\\Test02\\"
filenames = next(walk(data_path), (None, None, []))[2]  # [] if no file
nth = 25

df = pd.DataFrame()
for file in filenames:
    df_single = pd.read_csv(data_path + file, names=header)
    df_single.set_index("time")
    df = pd.concat([df, df_single], ignore_index=True)

df = df.iloc[::nth]

df_outdoor = df
df_outdoor = df_outdoor[df_outdoor["temp"] > -98]
df_outdoor = df_outdoor[df_outdoor["sensor_id"] == 0]
df_dateOnly = pd.to_datetime(df_outdoor["time"]).dt.date
dayChangeList_outdoor = df_dateOnly[df_dateOnly.diff() != "0 days"].index.tolist()

df_indoor = df
df_indoor = df_indoor[df_indoor["temp"] > -98]
df_indoor = df_indoor[df_indoor["sensor_id"] == 2]
df_dateOnly = pd.to_datetime(df_indoor["time"]).dt.date
dayChangeList_indoor = df_dateOnly[df_dateOnly.diff() != "0 days"].index.tolist()


fig1, axs = plt.subplots(2)
fig1.suptitle('Temperature')
axs[0].plot(df_outdoor["time"], df_outdoor["temp"], marker=".")
axs[0].set_title("Outdoor Temperature")
for day in dayChangeList_outdoor[1:]:
    axs[0].axvline(x = df_outdoor["time"].loc[day], color = 'k', label = 'axvline - full height')

axs[1].plot(df_indoor["time"], df_indoor["temp"], marker=".")
axs[1].set_title("Indoor Temperature")
for day in dayChangeList_indoor[1:]:
    axs[1].axvline(x = df_indoor["time"].loc[day], color = 'k', label = 'axvline - full height')

for ax in axs:
    plt.sca(ax)
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(5))
    plt.gca().axes.set_xlabel("Date (CET)")
    plt.gca().axes.set_ylabel("Temprature in °C")
    plt.gca().axes.set_ylim(-5,25)



########################################################################

df_outdoor = df
df_outdoor = df_outdoor[df_outdoor["humidity"] > -98]
df_outdoor = df_outdoor[df_outdoor["sensor_id"] == 0]
df_dateOnly = pd.to_datetime(df_outdoor["time"]).dt.date
dayChangeList_outdoor = df_dateOnly[df_dateOnly.diff() != "0 days"].index.tolist()

df_indoor = df
df_indoor = df_indoor[df_indoor["humidity"] > -98]
df_indoor = df_indoor[df_indoor["sensor_id"] == 2]
df_dateOnly = pd.to_datetime(df_indoor["time"]).dt.date
dayChangeList_indoor = df_dateOnly[df_dateOnly.diff() != "0 days"].index.tolist()

fig2, axs = plt.subplots(2)
axs[0].plot(df_outdoor["time"], df_outdoor["humidity"], marker=".")
axs[0].set_title("Outdoor humidity")
for day in dayChangeList_outdoor[1:]:
    axs[0].axvline(x = df_outdoor["time"].loc[day], color = 'k', label = 'axvline - full height')

axs[1].plot(df_indoor["time"], df_indoor["humidity"], marker=".")
axs[1].set_title("Indoor humidity")
for day in dayChangeList_indoor[1:]:
    axs[1].axvline(x = df_indoor["time"].loc[day], color = 'k', label = 'axvline - full height')


for ax in axs:
    plt.sca(ax)
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(5))
    plt.gca().axes.set_xlabel("Date (CET)")
    plt.gca().axes.set_ylabel("Humidity in %")
    plt.gca().axes.set_ylim(0,100)

plt.show()