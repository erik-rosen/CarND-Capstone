
GAS_DENSITY = 2.858
ONE_MPH = 0.44704


class Controller(object):
    def __init__(self, accel_limit, decel_limit):
        # TODO: Implement
        pass

    def control(self, linear_velocity_target, angular_velocity_target, velocity_actual):
        # TODO: Change the arg, kwarg list to suit your needs
        # Return throttle, brake, steer
        return 1., 0., 0.
