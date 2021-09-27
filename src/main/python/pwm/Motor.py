from enum import Enum


class Motor:
    class Direction(Enum):
        FORWARD = 'forward'
        REVERSE = 'backward'

    def run(self):
        pass

    def stop(self):
        pass

    def speed(self):
        pass

    def direction(self):
        pass
