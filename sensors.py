import RPi.GPIO as GPIO
import time

# Distance sensor
class DistanceSensor:
    def __init__(self, trig_pin=23, echo_pin=24):
        self.TRIG = trig_pin
        self.ECHO = echo_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)

    def read(self):
        # Trigger pulse
        GPIO.output(self.TRIG, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, False)
        start = time.time()
        stop = time.time()

        while GPIO.input(self.ECHO) == 0:
            start = time.time()
        while GPIO.input(self.ECHO) == 1:
            stop = time.time()
        distance = (stop - start) * 34300 / 2  # cm
        return distance

# Line sensors
class LineSensor:
    def __init__(self, pins=[5,6,13]):
        self.PINS = pins
        GPIO.setmode(GPIO.BCM)
        for pin in pins:
            GPIO.setup(pin, GPIO.IN)

    def read(self):
        return [GPIO.input(pin) for pin in self.PINS]

# IMU (gyro)
import smbus
class IMU:
    def __init__(self, addr=0x68):
        self.bus = smbus.SMBus(1)
        self.addr = addr
        self.bus.write_byte_data(self.addr, 0x6B, 0)  # Wake up

    def get_heading(self):
        # Simplified example
        return 0.0
