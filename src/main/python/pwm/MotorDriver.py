from .Motor import Motor


class MotorDriver:

    def drive(self, motor, speed, direction=Motor.Direction.FORWARD):
        pass

    def stop(self, motor):
        pass

    def to_json(self):
        pass
