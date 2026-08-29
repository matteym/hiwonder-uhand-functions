#!/usr/bin/python3
# coding=utf8
"""
Doigt d'honneur STREET + balancement lent gauche / droite
"""

import sys
import time

sys.path.append('/home/pi/uhandpi/common_sdk')
from common.ros_robot_controller_sdk import Board

THUMB, INDEX, MIDDLE, RING, PINKY, WRIST = 1, 2, 3, 4, 5, 6

CURL = {
    THUMB: 1800,
    INDEX: 1200,
    MIDDLE: 1200,
    RING: 1200,
    PINKY: 1200,
}

EXTEND = {
    THUMB: 900,     # légèrement tendu (style street)
    INDEX: 1200,
    MIDDLE: 1900,
    RING: 1200,
    PINKY: 1200,
}

WRIST_LEFT    = 900
WRIST_RIGHT   = 2100
WRIST_NEUTRAL = 1500

DURATION = 0.9          # lent

def set_middle_finger(board, wrist_pos, duration=DURATION):
    positions = [
        [THUMB,  EXTEND[THUMB]],
        [INDEX,  CURL[INDEX]],
        [MIDDLE, EXTEND[MIDDLE]],
        [RING,   CURL[RING]],
        [PINKY,  CURL[PINKY]],
        [WRIST,  wrist_pos],
    ]
    board.pwm_servo_set_position(duration, positions)
    time.sleep(duration)

def main():
    board = Board()
    try:
        print("Position de départ...")
        set_middle_finger(board, WRIST_NEUTRAL, duration=0.5)
        time.sleep(0.4)

        print("Doigt d'honneur STREET + balancement lent (Ctrl+C pour arrêter)")

        while True:
            set_middle_finger(board, WRIST_LEFT)
            set_middle_finger(board, WRIST_RIGHT)

    except KeyboardInterrupt:
        print("\nArrêt – retour neutre")
        set_middle_finger(board, WRIST_NEUTRAL, duration=0.5)

    finally:
        sys.exit(0)

if __name__ == '__main__':
    main()
