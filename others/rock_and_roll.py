#!/usr/bin/python3
# coding=utf8
"""
Geste "rock and roll" (cornes) pour uHandPi.
Index et auriculaire tendus, pouce/majeur/annulaire repliés.

A lancer depuis ~/uhandpi (ou en adaptant le sys.path.append ci-dessous)
pour que l'import de common.ros_robot_controller_sdk fonctionne.
"""
import sys
import time

sys.path.append('/home/pi/uhandpi/common_sdk')  # adapte si besoin
from common.ros_robot_controller_sdk import Board

# --- Mapping servo -> doigt (confirmé doc Hiwonder) ---
THUMB, INDEX, MIDDLE, RING, PINKY, WRIST = 1, 2, 3, 4, 5, 6

# Le pouce (servo 1) est monté à l'envers par rapport aux autres doigts.
# Si un doigt part dans le mauvais sens, inverse juste ses deux valeurs.
CURL = {
    THUMB:  1800,  # replié (sens inversé)
    INDEX:  1200,
    MIDDLE: 1200,
    RING:   1200,
    PINKY:  1200,
}
EXTEND = {
    THUMB:  900,  # tendu (sens inversé)
    INDEX:  1900,
    MIDDLE: 1800,
    RING:   1800,
    PINKY:  1900,
}
WRIST_NEUTRAL = 1500

DURATION = 0.4


def set_gesture(board, extended_fingers, duration=DURATION):
    positions = []
    for servo_id in (THUMB, INDEX, MIDDLE, RING, PINKY):
        pulse = EXTEND[servo_id] if servo_id in extended_fingers else CURL[servo_id]
        positions.append([servo_id, pulse])
    positions.append([WRIST, WRIST_NEUTRAL])
    board.pwm_servo_set_position(duration, positions)
    time.sleep(duration)


def main():
    board = Board()
    try:
        set_gesture(board, extended_fingers=[])
        time.sleep(0.3)

        # Signe rock and roll : index + auriculaire tendus
        set_gesture(board, extended_fingers=[INDEX, PINKY, THUMB])
        time.sleep(2)

        set_gesture(board, extended_fingers=[])
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
