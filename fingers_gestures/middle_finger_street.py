#!/usr/bin/python3
# coding=utf8
"""
Geste "doigt d'honneur" pour uHandPi.
Seul le majeur est tendu, les autres doigts sont repliés.

A lancer depuis ~/uhandpi (ou en adaptant le sys.path.append ci-dessous)
pour que l'import de common.ros_robot_controller_sdk fonctionne.
"""
import sys
import time

sys.path.append('/home/pi/uhandpi/common_sdk')  # adapte si besoin
from common.ros_robot_controller_sdk import Board

# --- Mapping servo -> doigt (confirmé doc Hiwonder) ---
# 1: pouce, 2: index, 3: majeur, 4: annulaire, 5: auriculaire, 6: poignet
THUMB, INDEX, MIDDLE, RING, PINKY, WRIST = 1, 2, 3, 4, 5, 6

# Pulses de base. Le pouce (servo 1) est monté à l'envers par rapport
# aux autres doigts -> ses valeurs replié/tendu sont inversées.
# Si un doigt part dans le mauvais sens, inverse juste ses deux valeurs.
CURL = {
    THUMB:  1800,  # replié (sens inversé)
    INDEX:  1200,  # replié
    MIDDLE: 1200,  # replié
    RING:   1200,  # replié
    PINKY:  1200,  # replié
}
EXTEND = {
    THUMB:  900,  # tendu (sens inversé)
    INDEX:  1800,  # tendu
    MIDDLE: 1900,  # tendu
    RING:   1800,  # tendu
    PINKY:  1800,  # tendu
}
WRIST_NEUTRAL = 1500

DURATION = 0.4  # secondes pour atteindre la position


def set_gesture(board, extended_fingers, duration=DURATION):
    """extended_fingers: liste des IDs de servo à tendre, les autres sont repliés."""
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
        # Position de repos avant le geste
        set_gesture(board, extended_fingers=[])
        time.sleep(0.3)

        # Doigt d'honneur : seul le majeur est tendu
        set_gesture(board, extended_fingers=[MIDDLE, THUMB])
        time.sleep(2)

        # Retour position neutre
        set_gesture(board, extended_fingers=[])
        time.sleep(0.5) 

    except KeyboardInterrupt:
        pass
    finally:

        sys.exit(0)


if __name__ == '__main__':
    main()
