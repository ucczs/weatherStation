from data_sink.sinkInterface import DataSink
import random
import time
import datetime

from paho.mqtt import client as mqtt_client


FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 12
MAX_RECONNECT_DELAY = 60
FLAG_EXIT = False


class mqttPublisher(DataSink):

    def __init__(self, broker: str, 
                 port: int, 
                 topic_temp_out: str, 
                 topic_temp_in: str, 
                 topic_humidity_in: str, 
                 topic_update_time: str, 
                 topic_co2_in: str, 
                 username_mqtt: str, 
                 password_mqtt: str) -> None:
        self.broker = broker
        self.port = port
        self.topic_temperature_out = topic_temp_out
        self.topic_temperature_in = topic_temp_in
        self.topic_humidity_in = topic_humidity_in
        self.topic_last_update = topic_update_time
        self.topic_co2_in = topic_co2_in

        self.client_id = f'publish-{random.randint(0, 1000)}'
        self.username_mqtt = username_mqtt
        self.password_mqtt = password_mqtt

        self.mqtt_client = self._connect_mqtt()
        self.mqtt_client.loop_start()

    def __del__(self):
        self.mqtt_client.loop_stop()

    def writeData(self, data: list[str], time: str = None) -> None:
        if time is None:
            time = str(datetime.datetime.now())

        sensor_data_string = "".join(data)
        if all([x in sensor_data_string for x in ["DHT20", "temperature"]]):
            result = self.mqtt_client.publish(self.topic_temperature_in, data[-1])

        if all([x in sensor_data_string for x in ["DHT20", "humidity"]]):
            result = self.mqtt_client.publish(self.topic_humidity_in, data[-1])

        if all([x in sensor_data_string for x in ["Weather API", "temperature"]]):
            result = self.mqtt_client.publish(self.topic_temperature_out, data[-1])

        if all([x in sensor_data_string for x in ["MH-Z19", "co2"]]):
            result = self.mqtt_client.publish(self.topic_co2_in, data[-1])

        if all([x in sensor_data_string for x in ["Dummy Sensor", "temperature"]]):
            result = self.mqtt_client.publish(self.topic_temperature_in, data[-1])
            result = self.mqtt_client.publish(self.topic_temperature_out, data[-1])

        result = self.mqtt_client.publish(self.topic_last_update, time)

    def _connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print(f"Failed to connect, return code {rc}")

        client = mqtt_client.Client(self.client_id)
        client.username_pw_set(self.username_mqtt, self.password_mqtt)
        client.on_connect = on_connect
        client.on_disconnect = self.on_disconnect
        client.connect(self.broker, self.port)
        return client

    def on_disconnect(self, client, userdata, rc):
        print(f"Disconnected with result code: {rc}")
        reconnect_count, reconnect_delay = 0, FIRST_RECONNECT_DELAY
        while reconnect_count < MAX_RECONNECT_COUNT:
            print(f"Reconnecting in {reconnect_delay} seconds...")
            time.sleep(reconnect_delay)

            try:
                client.reconnect()
                print("Reconnected successfully!")
                return
            except Exception as err:
                print(f"{err}. Reconnect failed. Retrying...")

            reconnect_delay *= RECONNECT_RATE
            reconnect_delay = min(reconnect_delay, MAX_RECONNECT_DELAY)
            reconnect_count += 1
        print("Reconnect failed after {reconnect_count} attempts. Exiting...")
        global FLAG_EXIT
        FLAG_EXIT = True
