import unittest

from main.python.pwm.TB6612FNG import TB6612FNG


class test_TB6612FNG(unittest.TestCase):

    def test_should_create_TB6612FNG_off(self):
        # Given
        motor_driver = TB6612FNG()
        # Then
        self.assertEqual(0, motor_driver.to_json()['reading']['value'])
