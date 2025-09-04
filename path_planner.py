class PathPlanner:
    def __init__(self):
        pass

    def compute(self, lane_error, pillar_info, heading):
        # Simplified example:
        target_speed = 50  # percent
        target_steer = lane_error * 0.1
        return target_speed, target_steer
