#!/usr/bin/python

from PCA9685 import PCA9685
import time
import json
from uuid import uuid4
from AwsIotCore import AwsIotCore

AWS_ENDPOINT = 'a12dev37b8fhwi-ats.iot.us-west-2.amazonaws.com'

writer = AwsIotCore(AWS_ENDPOINT)
writer.connect("tests-" + str(uuid4()))
message = {
    "address": "N/A",
    "addressType": "N/A",
    "name": "",
    "module": "Motor Driver",
    "version": "0.1",
    "reading": {}
}

Dir = [
    'forward',
    'backward',
]
pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)

direction = 'forward'
speed = 20
duration = 30

class MotorDriver():
    def __init__(self):
        self.PWMA = 0
        self.AIN1 = 1
        self.AIN2 = 2
        self.PWMB = 5
        self.BIN1 = 3
        self.BIN2 = 4

    def MotorRun(self, motor, index, speed):
        if speed > 100:
            return
        if(motor == 0):
            pwm.setDutycycle(self.PWMA, speed)
            if(index == Dir[0]):
                print ("#1 forward")
                pwm.setLevel(self.AIN1, 0)
                pwm.setLevel(self.AIN2, 1)
            else:
                print ("#1 backward")
                pwm.setLevel(self.AIN1, 1)
                pwm.setLevel(self.AIN2, 0)
        else:
            pwm.setDutycycle(self.PWMB, speed)
            if(index == Dir[0]):
                print ("#2 forward")
                pwm.setLevel(self.BIN1, 0)
                pwm.setLevel(self.BIN2, 1)
            else:
                print ("#2 backward")
                pwm.setLevel(self.BIN1, 1)
                pwm.setLevel(self.BIN2, 0)

    def MotorStop(self, motor):
        if (motor == 0):
            pwm.setDutycycle(self.PWMA, 0)
        else:
            pwm.setDutycycle(self.PWMB, 0)

print("this is a motor driver test code")
Motor = MotorDriver()

print('Running {} @ {} for {}s'.format(direction, speed, duration))

message['reading'] = {
    "value": speed,
    "timestamp": time.time()
}
writer.write('atlas', json.dumps(message, indent=4, default=str))

Motor.MotorRun(0, direction, speed)
Motor.MotorRun(1, direction, speed)
time.sleep(duration)

print("Stopping.")
Motor.MotorStop(0)
Motor.MotorStop(1)
message['reading'] = {
    "value": 0,
    "timestamp": time.time()
}
writer.write('atlas', json.dumps(message, indent=4, default=str))