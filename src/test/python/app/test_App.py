import unittest

from src.main.python.app.App import App


class test_App(unittest.TestCase):

    def test_should_create_motor_driver_off(self):
        # Given
        speed = 20
        duration = 30
        frequency = 60
        # When
        App(speed, duration, frequency)
        # Then
        # self.assertEqual(0, motor_driver.to_json()['reading']['value'])

    def test_should_run(self):
        # Given
        speed = 20
        duration = 30
        frequency = 60
        app = App(speed, duration, frequency)
        # When
        # TODO how to test long-running process?
        # app.start()
