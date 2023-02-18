import Adafruit_DHT
import time
import datetime

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PINS = [4, 5]
NEW_FILE_CNT = 3000

DATA_DIR = "/home/pi/weatherScripts/data/"

def readDataFromSensor(sensor_pin):
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, sensor_pin)
        if humidity is not None and temperature is not None:
                print("Sensor={0:0d}, Temp={1:0.1f}C, Humidity={2:0.1f}%".format(sensor_pin, temperature, humidity))
        else:
                humidity = None
                temperature = None

        return humidity, temperature

def writeDataToFile(humidity, temperature, sensor_pin, time, filename):
        with open(filename,'a') as file:
                file.write("{:s},{:d},{:f},{:f}\n".format(
                        time,
                        sensor_pin,
                        temperature,
                        humidity))


def getFilename():
        timestr = time.strftime("%Y%m%d-%H%M%S")
        filename = DATA_DIR + 'data_' + timestr + '.csv'
        return filename

def main():
        counter = 0
        filename = getFilename()

        while True:
                counter += 1
                if counter > NEW_FILE_CNT:
                        filename = getFilename()
                        counter = 0

                print("-"*40)
                currentTime = str(datetime.datetime.now())
                for DHT_PIN in DHT_PINS:
                        humidity, temperature = readDataFromSensor(DHT_PIN)
                        if (humidity is not None and temperature is not None):
                                writeDataToFile(humidity, temperature, DHT_PIN, currentTime, filename)
                        else:
                                writeDataToFile(-99, -99, DHT_PIN, currentTime, filename)
                                print("Sensor failure. Check wiring.")

                time.sleep(3)


if __name__ == "__main__":
        main()