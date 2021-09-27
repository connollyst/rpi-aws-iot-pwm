import time

from .Motor import Motor
from .MotorDriver import MotorDriver
from .PCA9685 import PCA9685


class TB6612FNG(MotorDriver):
    MAX_SPEED = 100
    PWM_FREQUENCY = 50
    PWMA = 0
    AIN1 = 1
    AIN2 = 2
    PWMB = 5
    BIN1 = 3
    BIN2 = 4

    def __init__(self):
        self._speed = 0  # There are multiple motors!
        self._pwm = PCA9685(0x40)
        self._pwm.set_pwm_frequency(self.PWM_FREQUENCY)

    def drive(self, motor, speed, direction=Motor.Direction.FORWARD):
        if speed > self.MAX_SPEED:
            raise Exception('Speed parameter {} exceeds max {}.', speed, self.MAX_SPEED)
        if motor == 0:
            self._drive(self.PWMA, self.AIN1, self.AIN2, direction, speed)
        elif motor == 1:
            self._drive(self.PWMB, self.BIN1, self.BIN2, direction, speed)
        else:
            raise Exception('Motor parameter out of bounds, expected 0 or 1 but received {}', motor)

    def _drive(self, pwm, in1, in2, direction, speed):
        if direction == Motor.Direction.FORWARD:
            self._pwm.set_duty_cycle(pwm, speed)
            self._pwm.set_level(in1, 0)
            self._pwm.set_level(in2, 1)
            self._speed = speed
        elif direction == Motor.Direction.REVERSE:
            self._pwm.set_duty_cycle(pwm, speed)
            self._pwm.set_level(in1, 1)
            self._pwm.set_level(in2, 0)
            self._speed = speed
        else:
            raise Exception('Unrecognized direction parameter: {}', direction.name)

    def stop(self, motor):
        if motor == 0:
            self._pwm.set_duty_cycle(self.PWMA, 0)
            self._speed = 0
        elif motor == 1:
            self._pwm.set_duty_cycle(self.PWMB, 0)
            self._speed = 0
        else:
            raise Exception('Motor parameter out of bounds, expected 0 or 1 but received {}', motor)

    def to_json(self):
        return {
            "address": "N/A",
            "addressType": "N/A",
            "name": "",
            "module": "Motor Driver",
            "version": "0.2",
            "reading": {
                "value": self._speed,
                "timestamp": time.time()
            }
        }
