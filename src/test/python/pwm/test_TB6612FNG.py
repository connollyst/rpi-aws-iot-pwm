import unittest

from src.main.python.pwm.TB6612FNG import TB6612FNG


class test_TB6612FNG(unittest.TestCase):

    def test_should_create_motor_driver_off(self):
        # When
        motor_driver = TB6612FNG()
        # Then
        self.assertEqual(0, motor_driver.to_json()['reading']['value'])

    def test_should_turn_motor_one_on(self):
        # Given
        motor_driver = TB6612FNG()
        # When
        motor_driver.drive(motor=0, speed=100)
        # Then
        self.assertEqual(100, motor_driver.to_json()['reading']['value'])

    def test_should_turn_motor_two_on(self):
        # Given
        motor_driver = TB6612FNG()
        # When
        motor_driver.drive(motor=1, speed=100)
        # Then
        self.assertEqual(100, motor_driver.to_json()['reading']['value'])

    def test_should_turn_motor_one_on_at_half_speed(self):
        # Given
        motor_driver = TB6612FNG()
        # When
        motor_driver.drive(motor=0, speed=50)
        # Then
        self.assertEqual(50, motor_driver.to_json()['reading']['value'])

    def test_should_turn_motor_two_on_at_half_speed(self):
        # Given
        motor_driver = TB6612FNG()
        # When
        motor_driver.drive(motor=1, speed=50)
        # Then
        self.assertEqual(50, motor_driver.to_json()['reading']['value'])

    def test_should_turn_motor_one_on_at_quarter_speed(self):
        # Given
        motor_driver = TB6612FNG()
        # When
        motor_driver.drive(motor=0, speed=25)
        # Then
        self.assertEqual(25, motor_driver.to_json()['reading']['value'])

    def test_should_turn_motor_two_on_at_quarter_speed(self):
        # Given
        motor_driver = TB6612FNG()
        # When
        motor_driver.drive(motor=1, speed=25)
        # Then
        self.assertEqual(25, motor_driver.to_json()['reading']['value'])

    def test_should_turn_motor_one_off(self):
        # Given
        motor_driver = TB6612FNG()
        # When
        motor_driver.stop(motor=0)
        # Then
        self.assertEqual(0, motor_driver.to_json()['reading']['value'])

    def test_should_turn_motor_two_off(self):
        # Given
        motor_driver = TB6612FNG()
        # When
        motor_driver.stop(motor=1)
        # Then
        self.assertEqual(0, motor_driver.to_json()['reading']['value'])
