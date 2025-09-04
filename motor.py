import RPi.GPIO as GPIO
import time

class MotorController:
    def __init__(self):
        self.PWM_PIN = 18  # GPIO pin for PWM
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PWM_PIN, GPIO.OUT)
        self.pwm = GPIO.PWM(self.PWM_PIN, 1000)  # 1kHz
        self.pwm.start(0)

    def set_speed(self, speed):
        """Speed: -100 to 100"""
        duty = max(min(abs(speed), 100), 0)
        self.pwm.ChangeDutyCycle(duty)
        # Add direction logic if using H-bridge

    def stop(self):
        self.pwm.ChangeDutyCycle(0)
        GPIO.cleanup()
