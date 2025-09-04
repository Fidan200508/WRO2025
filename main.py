import time
from drivers.motor import MotorController
from drivers.servo import ServoController
from drivers.sensors import DistanceSensor, LineSensor, IMU
from perception.lane_detection import LaneDetector
from perception.pillar_detection import PillarDetector
from planning.path_planner import PathPlanner
from control.speed_pid import SpeedPID
from control.steering_pid import SteeringPID


def main():
    print("Starting Raspberry Pi Self-Driving Car")

    # Initialize hardware
    motor = MotorController()
    servo = ServoController()
    distance = DistanceSensor()
    line_sensors = LineSensor()
    imu = IMU()

    # Initialize software modules
    lane_detector = LaneDetector()
    pillar_detector = PillarDetector()
    planner = PathPlanner()
    speed_pid = SpeedPID()
    steering_pid = SteeringPID()

    # Wait for start button (simulate for now)
    input("Press Enter to start autonomous mode...")

    try:
        while True:
            # Read sensors
            distance_data = distance.read()
            line_data = line_sensors.read()
            heading = imu.get_heading()

            # Perception
            lane_error = lane_detector.get_lane_error()
            pillar_info = pillar_detector.detect_pillars()

            # Planning
            target_speed, target_steer = planner.compute(lane_error, pillar_info, heading)

            # Control
            motor_pwm = speed_pid.update(target_speed)
            servo_angle = steering_pid.update(target_steer)

            # Drive
            motor.set_speed(motor_pwm)
            servo.set_angle(servo_angle)

            # Loop delay
            time.sleep(0.05)

    except KeyboardInterrupt:
        print("Stopping vehicle")
        motor.stop()
        servo.center()
