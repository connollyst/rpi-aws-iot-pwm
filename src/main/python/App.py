import json
import time
from uuid import uuid4

from aws.AwsIotCore import AwsIotCore
from pwm.MotorDriver import MotorDriver


class App:
    AWS_ENDPOINT = 'a12dev37b8fhwi-ats.iot.us-west-2.amazonaws.com'

    def __init__(self):
        self._direction = 'forward'
        self._speed = 20
        self._duration = 30
        self._frequency = 60

    def start(self):
        while True:
            self._run()
            time.sleep(self._frequency)

    def _run(self):
        print('Running {} @ {} for {}s'.format(self._direction, self._speed, self._duration))
        writer = AwsIotCore(self.AWS_ENDPOINT)
        writer.connect("tests-" + str(uuid4()))
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
        writer.write('atlas', json.dumps(message, indent=4, default=str))
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
        writer.write('atlas', json.dumps(message, indent=4, default=str))
