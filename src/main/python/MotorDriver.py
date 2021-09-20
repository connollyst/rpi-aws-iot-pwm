from PCA9685 import PCA9685


class MotorDriver:
    Dir = [
        'forward',
        'backward',
    ]

    def __init__(self):
        self.PWMA = 0
        self.AIN1 = 1
        self.AIN2 = 2
        self.PWMB = 5
        self.BIN1 = 3
        self.BIN2 = 4
        self._pwm = PCA9685(0x40, debug=False)
        self._pwm.setPWMFreq(50)

    def MotorRun(self, motor, index, speed):
        if speed > 100:
            return
        if (motor == 0):
            self._pwm.setDutycycle(self.PWMA, speed)
            if (index == self.Dir[0]):
                print("#1 forward")
                self._pwm.setLevel(self.AIN1, 0)
                self._pwm.setLevel(self.AIN2, 1)
            else:
                print("#1 backward")
                self._pwm.setLevel(self.AIN1, 1)
                self._pwm.setLevel(self.AIN2, 0)
        else:
            self._pwm.setDutycycle(self.PWMB, speed)
            if (index == self.Dir[0]):
                print("#2 forward")
                self._pwm.setLevel(self.BIN1, 0)
                self._pwm.setLevel(self.BIN2, 1)
            else:
                print("#2 backward")
                self._pwm.setLevel(self.BIN1, 1)
                self._pwm.setLevel(self.BIN2, 0)

    def MotorStop(self, motor):
        if (motor == 0):
            self._pwm.setDutycycle(self.PWMA, 0)
        else:
            self._pwm.setDutycycle(self.PWMB, 0)
