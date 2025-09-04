import RPi.GPIO as GPIO

class ServoController:
    def __init__(self):
        self.PIN = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN, GPIO.OUT)
        self.pwm = GPIO.PWM(self.PIN, 50)  # 50Hz
        self.pwm.start(7.5)  # Center position

    def set_angle(self, angle):
        """Angle in degrees: -45 (left) to +45 (right)"""
        duty = 7.5 + (angle / 18.0)
        self.pwm.ChangeDutyCycle(duty)

    def center(self):
        self.pwm.ChangeDutyCycle(7.5)
