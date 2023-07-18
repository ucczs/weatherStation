import datetime
import os
from data_sink.sinkInterface import DataSink

html_template = '''
<!DOCTYPE html>
<html>
<body>

<h1>Inside: DHT20_TEMP C</h1>
<h1>Outside: API_TEMP C</h1>
<h1>CO2 Inside: MH_Z19_CO2 ppm</h1>
<p>TIME</p>

</body>
</html>
'''

class staticHtmlWriter(DataSink):
    def __init__(self, file_dir: str, file_name: str = "index.html") -> None:
        self.file_name = file_name
        self.file_dir = file_dir
        self.dht20_temp_flag = False
        self.api_temp_flag = False
        self.mhz19_flag = False
        self.html_string = ""

    def writeData(self, data: list[str], time: str = None) -> None:
        if time is None:
            time = str(datetime.datetime.now())

        if not (self.dht20_temp_flag or self.api_temp_flag or self.mhz19_flag):
            self.html_string = html_template

        sensor_data_string = "".join(data)
        if all([x in sensor_data_string for x in ["DHT20", "temperature"]]):
            self.html_string = self.html_string.replace("DHT20_TEMP", data[-1])
            self.dht20_temp_flag = True

        if all([x in sensor_data_string for x in ["Weather API", "temperature"]]):
            self.html_string = self.html_string.replace("API_TEMP", data[-1])
            self.api_temp_flag = True

        if all([x in sensor_data_string for x in ["MH-Z19", "co2"]]):
            self.html_string = self.html_string.replace("MH_Z19_CO2", data[-1])
            self.mhz19_flag = True

        self.html_string = self.html_string.replace("TIME", time)

        if (self.dht20_temp_flag and self.api_temp_flag and self.mhz19_flag):
            self.dht20_temp_flag = False
            self.api_temp_flag = False
            self.mhz19_flag = False
            with open(os.path.join(self.file_dir, self.file_name), "w") as output_file:
                output_file.write(self.html_string)

