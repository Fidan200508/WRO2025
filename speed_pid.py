class SpeedPID:
    def __init__(self, Kp=1.0, Ki=0.0, Kd=0.1):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.prev_error = 0
        self.integral = 0

    def update(self, target):
        error = target
        self.integral += error
        derivative = error - self.prev_error
        self.prev_error = error
        return self.Kp*error + self.Ki*self.integral + self.Kd*derivative
