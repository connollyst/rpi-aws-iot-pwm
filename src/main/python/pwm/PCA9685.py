import math
import time

import smbus

from .Motor import Motor


# ============================================================================
# Raspi PCA9685 16-Channel PWM Servo Driver
# ============================================================================

class PCA9685(Motor):
    # Registers/etc.
    __SUBADR1 = 0x02
    __SUBADR2 = 0x03
    __SUBADR3 = 0x04
    __MODE1 = 0x00
    __PRESCALE = 0xFE
    __LED0_ON_L = 0x06
    __LED0_ON_H = 0x07
    __LED0_OFF_L = 0x08
    __LED0_OFF_H = 0x09
    __ALLLED_ON_L = 0xFA
    __ALLLED_ON_H = 0xFB
    __ALLLED_OFF_L = 0xFC
    __ALLLED_OFF_H = 0xFD

    def __init__(self, address, debug=False):
        self.bus = smbus.SMBus(1)
        self.address = address
        self.debug = debug
        if self.debug:
            print("Reseting PCA9685")
        self._write(self.__MODE1, 0x00)

    def set_pwm_frequency(self, freq):
        prescaleval = 25000000.0  # 25MHz
        prescaleval = prescaleval / 4096.0  # 12-bit
        prescaleval = prescaleval / float(freq)
        prescaleval = prescaleval - 1.0
        if self.debug:
            print("Setting PWM frequency to %d Hz" % freq)
            print("Estimated pre-scale: %d" % prescaleval)
        prescale = math.floor(prescaleval + 0.5)
        if self.debug:
            print("Final pre-scale: %d" % prescale)

        oldmode = self._read(self.__MODE1)
        newmode = (oldmode & 0x7F) | 0x10  # sleep
        self._write(self.__MODE1, newmode)  # go to sleep
        self._write(self.__PRESCALE, int(math.floor(prescale)))
        self._write(self.__MODE1, oldmode)
        time.sleep(0.005)
        self._write(self.__MODE1, oldmode | 0x80)

    def set_duty_cycle(self, channel, pulse):
        self._set_pwm(channel, 0, int(pulse * int(4096 / 100)))

    def set_level(self, channel, value):
        if (value == 1):
            self._set_pwm(channel, 0, 4095)
        else:
            self._set_pwm(channel, 0, 0)

    def _set_pwm(self, channel, on, off):
        "Sets a single PWM channel"
        self._write(self.__LED0_ON_L + 4 * channel, on & 0xFF)
        self._write(self.__LED0_ON_H + 4 * channel, 0xff & (on >> 8))
        self._write(self.__LED0_OFF_L + 4 * channel, off & 0xFF)
        self._write(self.__LED0_OFF_H + 4 * channel, 0xff & (off >> 8))
        if (self.debug):
            print("channel: %d  LED_ON: %d LED_OFF: %d" % (channel, on, off))

    def _write(self, reg, value):
        "Writes an 8-bit value to the specified register/address"
        self.bus.write_byte_data(self.address, reg, value)
        if (self.debug):
            print("I2C: Write 0x%02X to register 0x%02X" % (value, reg))

    def _read(self, reg):
        "Read an unsigned byte from the I2C device"
        result = self.bus.read_byte_data(self.address, reg)
        if (self.debug):
            print("I2C: Device 0x%02X returned 0x%02X from reg 0x%02X" % (self.address, result & 0xFF, reg))
        return result

# pwm = PCA9685(0x5f, debug=False)
# pwm.setPWMFreq(50)
# pwm.setDutycycle(0,100)
# pwm.setLevel(1,0)
# pwm.setLevel(2,1)
