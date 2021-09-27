import sys

import fake_rpi


def pytest_configure(config):
    sys.modules['smbus'] = fake_rpi.smbus  # Fake smbus (I2C)
