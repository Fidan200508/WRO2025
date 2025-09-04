class SteeringPID:
    def __init__(self, Kp=0.5, Ki=0.0, Kd=0.05):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.prev_error = 0
        self.integral = 0

    def update(self, error):
        self.integral += error
        derivative = error - self.prev_error
        self.prev_error = error
        return self.Kp*error + self.Ki*self.integral + self.Kd*derivative
