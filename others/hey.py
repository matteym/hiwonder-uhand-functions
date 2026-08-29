#!/usr/init/python3
# coding=utf8
import sys
import time

sys.path.append('/home/pi/uhandpi/common_sdk')
from common.ros_robot_controller_sdk import Board

THUMB, INDEX, MIDDLE, RING, PINKY, WRIST = 1, 2, 3, 4, 5, 6

def main():
    board = Board()
    OPEN = [[THUMB, 1200], [INDEX, 1800], [MIDDLE, 1800], [RING, 1800], [PINKY, 1800]]
    SLIGHT_CLOSE = [[THUMB, 1200], [INDEX, 1700], [MIDDLE, 1700], [RING, 1700], [PINKY, 1700]]

    print("Salut parfait lancé ! (Ctrl+C pour arrêter)")
    try:
        while True:
            board.pwm_servo_set_position(0.4, OPEN + [[WRIST, 1800]])
            time.sleep(0.5)
            board.pwm_servo_set_position(0.4, SLIGHT_CLOSE + [[WRIST, 1500]])
            time.sleep(0.5)
            board.pwm_servo_set_position(0.4, OPEN + [[WRIST, 1200]])
            time.sleep(0.5)
            board.pwm_servo_set_position(0.4, SLIGHT_CLOSE + [[WRIST, 1500]])
            time.sleep(0.5)
    except KeyboardInterrupt:
        board.pwm_servo_set_position(0.5, [[1, 1500], [2, 1500], [3, 1500], [4, 1500], [5, 1500], [6, 1500]])
        print("\nArrêt du salut.")
        sys.exit(0)

if __name__ == '__main__':
    main()
