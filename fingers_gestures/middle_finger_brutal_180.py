#!/usr/bin/python3
# coding=utf8
"""
Doigt d'honneur BRUTAL + balancement lent gauche / droite
(version plus agressive : pouce bien replié, majeur ultra tendu)
"""

import sys
import time

sys.path.append('/home/pi/uhandpi/common_sdk')
from common.ros_robot_controller_sdk import Board

THUMB, INDEX, MIDDLE, RING, PINKY, WRIST = 1, 2, 3, 4, 5, 6

CURL = {
    THUMB: 1800,
    INDEX: 1100,    # bien fermé
    MIDDLE: 1100,
    RING: 1100,
    PINKY: 1100,
}

EXTEND = {
    THUMB: 1800,    # pouce bien replié (style brutal)
    INDEX: 1100,
    MIDDLE: 1950,   # majeur ultra tendu
    RING: 1100,
    PINKY: 1100,
}

WRIST_LEFT    = 900
WRIST_RIGHT   = 2100
WRIST_NEUTRAL = 1500

DURATION = 0.9          # lent

def set_middle_finger(board, wrist_pos, duration=DURATION):
    positions = [
        [THUMB,  CURL[THUMB]],
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

        print("Doigt d'honneur BRUTAL + balancement lent (Ctrl+C pour arrêter)")

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
