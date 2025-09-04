Raspberry Pi Self-Driving Car – WRO Future Engineers
Team Name: RoboMotion
Country: Azerbaijan
Project: WRO Future Engineers 2025 / Self-driving Car
1. Project Overview

This project presents a 4-wheeled autonomous vehicle built on a Raspberry Pi platform, capable of performing Open Challenge and Obstacle Challenge tasks for the WRO Future Engineers competition. The vehicle is equipped with a servo-based steering system, DC gear motor drive, and a variety of sensors including:

Distance Sensor (Ultrasonic) for obstacle detection

Line Sensor Array for lane tracking

Gyro/IMU for heading and orientation control

Camera for lane and pillar detection

The main goals of the project were to design a reliable autonomous driving system, implement a modular software architecture, and provide full engineering documentation on GitHub to inspire and guide future teams.

2. Motivation

The motivation behind this project was to explore autonomous vehicle control at a small scale, integrating mechanical design, electronics, and AI-based perception. We aimed to:

Develop a vehicle that can navigate complex tracks autonomously.

Implement sensor fusion and PID control for precise motion and steering.

Provide a comprehensive GitHub repository for future engineers.

3. Vehicle Mobility & Power

Drive System: Single DC gear motor connected to the rear wheels.

Steering: Servo motor with 45° left/right range.

Power Supply: 7.4V Li-ion battery pack, powering motor and Raspberry Pi.

Chassis: Lightweight 3D-printed frame; total weight ≤ 1.5 kg.

4. Sensors & Perception

Distance Sensor (Ultrasonic HC-SR04): Detects obstacles and measures proximity.

Line Sensor Array: Three digital IR sensors for lane detection.

Gyroscope/IMU: Provides orientation and heading data for stabilization.

Camera (Pi Camera Module): Detects lanes, red and green pillars for obstacle challenge.

5. Software Architecture

The software is modular and consists of the following components:

Module	Description
drivers/	Low-level control of motors, servo, and sensors
perception/	Computer vision: lane and pillar detection
planning/	Path planning and high-level state machine
control/	PID controllers for speed and steering
utils/	Logging, configuration, and helper functions
tests/	Unit tests for individual modules
main.py	Orchestrates all modules and runs autonomous driving loop
6. Vehicle Operation

Starting Procedure: Press ON button, then Start button to enter autonomous mode.

Open Challenge: Vehicle completes three laps, tracks lanes without traffic signs.

Obstacle Challenge: Vehicle completes three laps with randomly placed red/green pillars, and performs parallel parking in designated parking lot.

Constraints: Vehicle must not exceed 300x200x300 mm, weight ≤ 1.5 kg.

7. Control & Algorithms

Speed PID: Maintains target speed based on path planning.

Steering PID: Controls servo to correct lane error.

Lane Detection: Uses Canny edge detection and center-line calculation.

Pillar Detection: Detects red and green pillars using HSV thresholding.

Path Planning: Determines optimal speed and steering angle using sensor and perception input.

8. Build & Run Instructions

Clone the repository:

git clone https://github.com/YourUsername/RPi-SelfDrivingCar.git
cd RPi-SelfDrivingCar/software


Install dependencies:

pip install -r requirements.txt


Run the main program:

python main.py


Press Enter to start autonomous driving.

Logs and sensor outputs are saved in /logs for analysis.

9. Documentation & Media

Vehicle Photo in 3D

We created this model on Tinkercad 3D program.

10. GitHub Commit History

First commit: ≥ 1/5 of code, ≥ 2 months before competition.

Second commit: ≥ 1 month before competition.

Third commit: ≥ 2 weeks before competition.

Additional commits allowed to show development progress.

11. Notes

All software is written in Python and designed for Raspberry Pi 5.

Code is fully commented and modular for easy understanding.

Repository is public to encourage learning and sharing among WRO participants.

12. References

Raspberry Pi Documentation

HC-SR04 Distance Sensor Datasheet

Servo Motor Control with Raspberry Pi

World Robot Olympiad Future Engineers Rules
