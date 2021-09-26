import json
import time
from uuid import uuid4

from Logger import get_logger
from aws.AwsIotCore import AwsIotCore
from pwm.MotorDriver import MotorDriver


class App:
    LOGGER = get_logger(__name__)

    AWS_ENDPOINT = 'a12dev37b8fhwi-ats.iot.us-west-2.amazonaws.com'
    AWS_IOT_MQTT_TOPIC = 'atlas'  # 'iot/devices/readings'
    AWS_CLIENT_ID = "iot-motor-" + str(uuid4())

    def __init__(self, speed, duration, frequency):
        self._direction = MotorDriver.Direction.FORWARD
        self._speed = speed
        self._duration = duration
        self._frequency = frequency

    def start(self):
        while True:
            self._run()
            time.sleep(self._frequency)

    def _run(self):
        print('Running {} @ {} for {}s'.format(self._direction, self._speed, self._duration))
        writer = AwsIotCore(self.AWS_ENDPOINT)
        writer.connect(self.AWS_CLIENT_ID)
        message = {
            "address": "N/A",
            "addressType": "N/A",
            "name": "",
            "module": "Motor Driver",
            "version": "0.1",
            "reading": {}
        }
        motor = MotorDriver()
        message['reading'] = {
            "value": self._speed,
            "timestamp": time.time()
        }
        writer.write(self.AWS_IOT_MQTT_TOPIC, json.dumps(message, indent=4, default=str))
        motor.run(0, self._direction, self._speed)
        motor.run(1, self._direction, self._speed)
        time.sleep(self._duration)
        print("Stopping.")
        motor.stop(0)
        motor.stop(1)
        message['reading'] = {
            "value": 0,
            "timestamp": time.time()
        }
        writer.write(self.AWS_IOT_MQTT_TOPIC, json.dumps(message, indent=4, default=str))
